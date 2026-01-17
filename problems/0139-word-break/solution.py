class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.approach_2(s, wordDict)

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
        """
        Approach :

        Backtracking
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
