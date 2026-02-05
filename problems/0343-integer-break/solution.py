class Solution:
    def integerBreak(self, n: int) -> int:
        return self.approach_3(n)

    def approach_3(self, n: int) -> int:
        '''
        Time Complexity : O(n^2)
        Space Complexity : O(n) for DP array
        '''
        '''
        Approach: Iterative DP - Bottom-up

        Recurrence Relation :

        State Definition :

        dp(i) = maximum product obtainable by breaking integer 'i' into at least two positive integers,
        for each integer from 1 to 'i'

        Base case :

        dp(1) = 1, maximum product for each integer from 1 to 1 is 1. Integer 1 cannot be broken, 
        so its “integer break” product is undefined.

        Recurrence :

        ∀ i >= 2:
        
        dp[i] = max(dp[i], 
                    j * (i - j), # no further split -> stop splitting
                    j * dp[i - j] # further split -> continue splitting optimally
                )
        , where j ∈ [1,i)

        Intuition :

        For any number i, the best way to break it must involve choosing a first cut at some position j,
        and then deciding:
        'Do we stop here, or do I keep breaking the remaining part optimally?'

        For every integer 'i', we try all possible first cuts 'j'.
        For each cut, we either stop and multiply directly, or 
        reuse the already-optimal product of the remaining part.
        Taking the maximum over all such choices guarantees the best result.

        Boundary Condition :

        i >= 2
        j ∈ [1, i - 1]

        DP state Table :
	
        i : 1;	–	; dp[i] :1
        i : 2;	Best split(s) : 1 + 1 -> 1×1; dp[i] : 1
        i : 3;	Best split(s) : 1 + 2 -> 1×2; dp[i] : 2
        i : 4;	Best split(s) : 2 + 2 -> 2×2; dp[i] : 4
        i : 5;	Best split(s) : 2 + 3 -> 2×3; dp[i] : 6
        i : 6;	Best split(s) : 3 + 3 -> 3×3; dp[i] : 9
        i : 7;	Best split(s) : 3 + 4 -> 3×4; dp[i] : 12
        i : 8;	Best split(s) : 3 + 3 + 2 -> 3×3×2; dp[i] :	18
        i : 9;	Best split(s) : 3 + 3 + 3 -> 3×3×3; dp[i] :	27
        i : 10;	Best split(s) : 3 + 3 + 4 -> 3×3×4; dp[i] :	36

        for i = 8,

        j : 1; Expression: 1 × max(7, dp[7]=12); Value : 12
        j : 2; Expression: 2 × max(6, dp[6]=9); Value :18 -> max
        j : 3; Expression: 3 × max(5, dp[5]=6); Value :18 -> max
        j : 4; Expression: 4 × max(4, dp[4]=4); Value :16
        j : 5; Expression: 5 × max(3, dp[3]=2); Value :15
        j : 6; Expression: 6 × max(2, dp[2]=1); Value :12
        j : 7; Expression: 7 × max(1, dp[1]=1); Value :7

        so, 
        dp[8] = 18

        '''
        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = float('-inf')

            for j in range(1, i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
    
        return dp[n]

    def approach_2(self, n: int) -> int:
        '''
        Time Complexity : O(n^2)
        Space Complexity : O(n) for call stack
        '''
        '''
        Approach: DFS with Memoization / Top-Down 

        For each split i + (n - i):
        - stop splitting: i * (n - i)
        - keep splitting: i * dfs(n - i)
        '''

        dp = [-1] * (n + 1)

        def dfs(n):
            if dp[n] != -1:
                return dp[n]

            if n == 1:
                return 1

            result = float('-inf')

            for i in range(1, n):
                result = max(result, i * dfs(n - i), i * (n - i))

            dp[n] = result
            return result
        
        return dfs(n)

    def approach_1(self, n: int) -> int:
        '''
        Time Complexity : O(2^n)
        Space Complexity : O(n) for call stack
        '''
        '''
        Approach: DFS

        For each split i + (n - i):
        - stop splitting: i * (n - i)
        - keep splitting: i * dfs(n - i)
        '''
        def dfs(n):
            if n == 1:
                return 1
            result = float('-inf')
            for i in range(1, n):
                result = max(result, i * dfs(n - i), i * (n - i))
            return result
        
        return dfs(n)
