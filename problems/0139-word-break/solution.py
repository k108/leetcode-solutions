class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Time Complexity : O(W*L), where 
        W is the number of words, and 
        L is an average length of the word
        """
        current_node = self.root
        for c in word:
            if c not in current_node.children:
                current_node.children[c] = TrieNode()
            current_node = current_node.children[c]
        current_node.end_of_word = True

    def search(self, word: str) -> bool:
        """
        Time Complexity : O(W*L), where 
        W is the number of words, and 
        L is an average length of the word
        """
        current_node = self.root
        for c in word:
            if c not in current_node.children:
                return False
            current_node = current_node.children[c]
        return current_node.end_of_word
        

    def startsWith(self, prefix: str) -> bool:
        """
        Time Complexity : O(W*L), where 
        W is the number of words, and 
        L is an average length of the word
        """
        current_node = self.root
        for c in prefix:
            if c not in current_node.children:
                return False
            current_node = current_node.children[c]
        return True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.approach_6(s, wordDict)

    def approach_6(self, s: str, wordDict: List[str]) -> bool:
        """
        Time Complexity : O(N^3) or O(N^2)
        Each index processed once → O(N) states
        From each index, try all j ≥ i → O(N)
        Substring cost → O(N) (Python)
        
        If substring slicing were O(1): O(N^2)

        Space Complexity : O(N), Queue and visited set
        """
        """
        Approach : BFS
        """
        N = len(s)
        word_set = set(wordDict)
        # start index positions to explore
        queue = deque([0])
        # avoid re-processing the same index
        visited = set()

        while queue:
            start = queue.popleft()

            if start == N:
                return True

            if start in visited:
                continue
            visited.add(start)

            for end in range(start, N):
                if s[start:end+1] in word_set:
                    queue.append(end+1)

        return False

    def approach_5(self, s: str, wordDict: List[str]) -> bool:
        """
        Time complexity: O(n^2 + m*k) or O(n*L + m*k)

        Let:
        n = length of string
        m = number of words
        k = average word length
        L = maximum word length in dictionary
        
        Building the trie involves iterating over all characters of all words. This costs O(m*k).
        
        Once we build the trie, we calculate dp. For each i, we iterate over all the indices after i. 
        We have a basic nested for loop which costs O(n^2) to handle all dp[i].

        For each valid dp[i], we walk forward in the Trie. Trie walk stops after at most L characters.
        Each character is processed once per start position.
        
        Space complexity: O(n + m*k)
        
        The dp array takes O(n) space. The trie can have up to m*k nodes in it.
        """
        """
        Approach : Trie

        dp[j] |= dp[i] AND (s[i:j] in wordDict)

        """
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        N = len(s)
        dp = [False] * (N + 1)
        dp[0] = True
        for i in range(0, N+1):
            if dp[i]:
                # Start at Trie root where dp[i] is True
                curr = trie.root
                for j in range(i, N):
                    c = s[j]
                    if c not in curr.children:
                        # If the character is not a child in Trie -> stop
                        # No words exist
                        break
                    
                    curr = curr.children[c]
                    # s[i:j) is a dictionary word
                    # set dp[j] = True
                    if curr.end_of_word:
                        dp[j+1] = True

        return dp[N]

    def approach_4(self, s: str, wordDict: List[str]) -> bool:
        """
        Time Complexity : O(N*M*K); N is the length of s, M is the length of wordDict, and 
        M is the average length of the words in wordDict

        Space Complexity : O(N), for dp array
        """
        N = len(s)
        dp = [False] * (N + 1)
        dp[0] = True
        for i in range(1, N+1):
            for word in wordDict:
                cur_len = len(word)
                if i >= cur_len:
                    j = i-cur_len
                    if dp[j] == True and word == s[j:i]:
                        dp[i] = True
        return dp[N]

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
        """
        Approach : Memoization
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
        Approach : DFS
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
