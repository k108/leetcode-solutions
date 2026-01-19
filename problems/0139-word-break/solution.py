class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.approach_3(s, wordDict)

    def approach_3(self, s: str, wordDict: List[str]) -> bool:
        """
        Time Complexity : O(N^2) or O(N^3), O(N) dfs states * O(N^2) work per state

        Space Complexity : O(N), for dp array
        """
        """
        Approach :

        Iterative DP

        State Definition :

        Let dp[i] be a boolean value such that:

        dp[i] = True if the prefix s[0 : i] can be segmented into valid dictionary words.

        Base Case :

        dp[0] = True

        Reason:
        - The empty string is trivially breakable
        - Enables words to start at index 0
        ("" + first_word)

        Recurrence Relation :
        
        For i ≥ 1:

        dp[i] = OR over all j in [0, i):

                dp[j] AND ( s[j : i] ∈ wordDict )

        Meaning:
        - We try all possible last cut positions j
        - s[0 : i] is breakable if there exists a j such that:
            - the prefix s[0 : j] is already breakable
            - the suffix s[j : i] is a single dictionary word


        Boundary Conditions :

        - j < i ensures s[j : i) is non-empty
        - dp[j] must be evaluated before dp[i]
        → DP must be computed in increasing order of i
        - If dp[i] becomes True for any j, further checks can stop


        DP Table Trace :

        s = "abcdef"
        wordDict = {"ab", "cd", "ef"}

        Indices:
        i :   0   1   2   3   4   5   6
        s :       a   b   c   d   e   f
        dp:   T   F   T   F   T   F   T


        i=0; j=0; dp[0] = True    # empty string

        i = 2; j = 0 -> dp[0] = True, s[0:2] = "ab" ∈ dict -> dp[2] = True

        i = 4; j = 2 -> dp[2] = True, s[2:4] = "cd" ∈ dict -> dp[4] = True

        i = 6; j = 4 -> dp[4] = True, s[4:6] = "ef" ∈ dict -> dp[6] = True

        Final Answer:
        dp[n] = dp[6] = True
        """
        N = len(s)
        word_set = set(wordDict)
        dp = [False]*(N+1)
        # Empty string is trivially breakable
        dp[0] = True

        for i in range(1, N+1):
            for j in range(0, i):
                # s1 = s[0:j] = dp[j]
                # s2 = s[j:i]
                if dp[j] and (s[j:i] in word_set):
                    dp[i] = True
                    break
        
        return dp[N]

    def approach_2(self, s: str, wordDict: List[str]) -> bool:
        """
        Time Complexity : O(N^2) or O(N^3), O(N) dfs states * O(N^2) work per state

        Space Complexity : O(N), for dp array and recursion stack
        """
        N = len(s)
        word_set = set(wordDict)

        def dfs(i, dp):
            if i==N:
                return True
            
            if dp[i] != None:
                return dp[i]

            for j in range(i, N):
                if s[i:j+1] in word_set:
                    if dfs(j+1, dp):
                        dp[i] = True
                        return dp[i]

            dp[i] = False
            return dp[i]

        return dfs(0, [None]*N)

    def approach_1(self, s: str, wordDict: List[str]) -> bool:
        """
        Time Complexity : O(N^N), each time we have at most N choices and depth is N
        or O(N^2 * 2^N), partition a string O(2^N) & substring O(N)

        Space Complexity : O(N), string length and call stack depth
        """

        N = len(s)
        word_set = set(wordDict)

        def dfs(i):
            if i==N:
                return True

            for j in range(i, N):
                if s[i:j+1] in word_set:
                    if dfs(j+1):
                        return True
            return False

        return dfs(0)
