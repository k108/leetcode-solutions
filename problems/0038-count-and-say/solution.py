class Solution:
    def rle(self, s):
        result = []
        freq = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                freq +=1
            else:
                result.append(f'{freq}{s[i - 1]}')
                freq = 1

        result.append(f'{freq}{s[-1]}')

        return ''.join(result)

    def countAndSay(self, n: int) -> str:
        '''
        Time Complexity : O(n)
        Space Complexity : O(n)
        '''
        dp = [''] * (n + 1)
        dp[1] = '1'

        for i in range(2, n + 1):
            # prev = dp[i - 1]
            # current = []
            # count = 1

            # # Loop through previous string and perform run-length encoding
            # for j in range(1, len(prev)):
            #     if prev[j] == prev[j - 1]:
            #         count += 1
            #     else:
            #         # Append count + digit (e.g., 3 + '1' = '31')
            #         current.append(str(count))
            #         current.append(prev[j - 1])
            #         count = 1

            # # Don’t forget the last run
            # current.append(str(count))
            # current.append(prev[-1])

            # # Join all parts into one string
            # dp[i] = ''.join(current)
            dp[i] = self.rle(dp[i-1])

        return dp[n]
