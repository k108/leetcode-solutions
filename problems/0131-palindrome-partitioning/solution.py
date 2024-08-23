class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        Time Complexity : O(2^N)
        """
        N = len(s)
        result = []
        def check_palindrome(word, i, j):
            while(i<j):
                if word[i]!=word[j]:
                    return False
                i+=1
                j-=1
            return True

        def dfs(i, part):
            if i>=N:
                result.append(part.copy())
                return

            for j in range(i, N):
                if check_palindrome(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1, part)
                    part.pop()

        dfs(0, [])
        return result
