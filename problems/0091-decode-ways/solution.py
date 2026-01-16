class Solution:
    def numDecodings(self, s: str) -> int:
        return self.approach_3(s)

    def approach_3(self, s: str) -> int:
        '''
        Time complexity: O(n)
        Space complexity: O(1)
        '''
        '''
        Approach :

        Fibonacci-style DP
        We process the string from right to left and maintain only
        the last two DP states instead of a full DP array
        '''
        # number of ways to decode substring starting at i+1
        # represents dp[i+1]
        # Base case: dp[n] = 1 (empty string has exactly one valid decoding)
        dp_1 = 1

        # number of ways to decode substring starting at i+2
        # represents dp[i+2]
        # Initialized to 0 because dp[n+1] is never used meaningfully
        dp_2 = 0

        # Traverse the string from right to left
        for i in range(len(s)-1, -1, -1):
            # substring starting with '0' is not a valid encoding
            if s[i] == '0':
                # number of ways to decode substring starting at i
                dp = 0
            else:
                dp = dp_1
                if i < len(s)-1 and (s[i]=='1' or (s[i]=='2' and s[i+1]<'7')):
                    # Add number of ways to decode the remaining substring
                    dp += dp_2
            
            # Shift the DP window:
            # dp[i+2] becomes dp[i+1]
            # dp[i+1] becomes dp[i]
            dp_2 = dp_1
            dp_1 = dp
        
        return dp_1 if len(s) != 0 else 0

    def approach_2(self, s: str) -> int:
        '''
        Time complexity: O(n)
        Space complexity: O(n)
        '''
        '''
        Approach :

        Bottom-up dynamic programming using a DP array
        dp[i] represents the number of ways to decode substring s[i:]
        '''
        # dp[i] = number of ways to decode substring starting at index i
        dp = [-1]*(len(s)+1)

        # Base case: dp[n] = 1 (empty string)
        dp[len(s)] = 1

        # Fill the DP table from right to left
        for i in range(len(s)-1, -1, -1):
            # substring starting with '0' is not a valid encoding
            if s[i] == '0':
                dp[i] = 0
            else:
                # Decode one character
                dp[i] = dp[i+1]
                # Decode two characters if valid ("10" to "26")
                if i < len(s)-1 and (s[i]=='1' or (s[i]=='2' and s[i+1]<'7')):
                    dp[i] += dp[i+2]

        # dp[0] gives the total number of ways to decode the full string
        return dp[0] if len(s)!=0 else 0
    
    def approach_1(self, s: str) -> int:
        '''
        Time complexity: O(n)
        Space complexity: O(n)
        '''
        '''
        Approach : 

        Top-down DFS + memoization
        dfs(i) returns the number of ways to decode substring s[i:]

        State definition : 
        Let dp[i] = number of ways to decode the substring s[i:]

        Base case : 
        dp[n] = 1, i.e. an empty string has exactly one valid decoding
        (we successfully decoded everything)

        Recurrence Relation :
        For 0 ≤ i < n :
        Case 1 : dp[i] = 0, s[i] == '0'
        Case 2 : s[i] != '0'
        dp[i] = dp[i+1] + dp[i+2], 10 ≤ s[i:i+2] ≤26
        dp[i] = dp[i+1], otherwise

        Boundary Conditions :
        dp[n] = 1
        dp[n+1] is treated as 0 (only needed conceptually)

        Example :
        s = "226"
        i = 3 ; s[i:] = "" ; dp[i] = 1
        i = 2 ; s[i:] = "6" ; dp[i] = dp[3] = 1
        i = 1 ; s[i:] = "26" ; dp[i] = dp[2] + dp[3] = 2
        i = 0 ; s[i:] = "226" ; dp[i] = dp[1] + dp[2] = 3
        '''

        def dfs(i, dp):
            # If we've reached the end of the string,
            # we've found one valid decoding
            # count as 1 way to decode
            if i == len(s):
                return 1

            # substring starting with '0' is not a valid encoding
            if s[i] == '0':
                return 0

            if dp[i] != -1:
                return dp[i]

            # Decode one character
            res = dfs(i+1, dp)
            
            # Decode two characters if valid ("10" to "26")
            if i < len(s)-1 and (s[i]=='1' or (s[i]=='2' and s[i+1]<'7')):
                res += dfs(i+2, dp)

            dp[i] = res

            return res
        
        return dfs(0, [-1]*len(s)) if len(s)!=0 else 0
