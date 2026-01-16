class Solution:
    def numDecodings(self, s: str) -> int:
        return self.approach_1(s)

    def approach_2(self, s: str) -> int:
        pass
    
    def approach_1(self, s: str) -> int:
        '''
        Time complexity: O(n)
        Space complexity: O(n)
        '''

        def dfs(i, dp):
            # count as 1 way to decode
            if i == len(s):
                return 1

            # substring starting with '0' is not a valid encoding
            if s[i] == '0':
                return 0

            if dp[i] != -1:
                return dp[i]

            res = dfs(i+1, dp)

            if i < len(s)-1 and (s[i]=='1' or (s[i]=='2' and s[i+1]<'7')):
                res += dfs(i+2, dp)

            dp[i] = res

            return res
        
        return dfs(0, [-1]*len(s)) if len(s)!=0 else 0
