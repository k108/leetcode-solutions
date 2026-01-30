class Solution:
    def numSquares(self, n: int) -> int:
        return self.approach_2(n)

    def approach_2(self, n: int) -> int:
        '''
        Time Complexity = O(n * (n^1/2))
        Space Complexity = O(n)
        '''
        '''
        Approach : Memoization

        '''
        dp = [-1] * (n + 1)

        def dfs(n):
            if n == 0: 
                return 0

            if dp[n] != -1:
                return dp[n]

            ans = float('inf')
            i = 1
            while i * i <= n:
                sq = i * i
                ans = min(ans, 1 + dfs(n - sq))
                i += 1
            dp[n] = ans

            return ans

        return dfs(n)
    
    def approach_1(self, n: int) -> int:
        '''
        Time Complexity = O((n^1/2)^n)
        Space Complexity = O(n)
        '''
        '''
        Intuition :

        We can always construct using 1

        If we choose one square now, what remains is the same problem for a smaller number.
        Each “remaining” is again: least number of squares that sum to that value.

        n = 12
        Pick 4 -> remaining = 8
        Pick 9 -> remaining = 3
        Pick 1 -> remaining = 11

        For n, we can try every sq ≤ n; sq ∈ {1², 2², 3², ...} and sq ≤ n :
        n = sq + remainder
        n - sq = remainder
        ans(n - sq) = ans(remainder)
        ans(n) = 1 (for sq) + answer(n - sq)

        n = 13
        13 = 1 + 12 -> 1 + answer(12)
        13 = 4 + 9  -> 1 + answer(9)
        13 = 9 + 4  -> 1 + answer(4)

        sq = 1² → 1 + answer(n - 1)
        sq = 2² → 1 + answer(n - 4)
        sq = 3² → 1 + answer(n - 9)

        answer(n) = min over all sq ≤ n of (1 + answer(n - sq))
        answer(n) = 1 + min(answer(n - sq))

        We must pick one square at the current step
        That square contributes exactly 1 to the count
        Everything else is handled optimally by answer(n - sq)
        '''
        def dfs(n):
            if n == 0: 
                return 0
            ans = float('inf')
            i = 1
            while i * i <= n:
                sq = i * i
                ans = min(ans, 1 + dfs(n - sq))
                i += 1
            return ans

        return dfs(n)
