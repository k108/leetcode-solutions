import math

class Solution:
    def numSquares(self, n: int) -> int:
        return self.approach_5(n)

    def approach_5(self, n: int) -> int:
        '''
        Time Complexity = O(n^(1/2))
        Space Complexity = O(1)
        '''
        '''
        Approach :
        Lagrange's four-square theorem :
        Every positive integer can be written as the sum of at most four perfect squares.
        That means the answer is always in {1, 2, 3, 4}.

        Legendre's three-square theorem :
        Use Legendre’s Three Square Theorem
        A number cannot be written as the sum of three squares iff,
        n = 4^k * ((8 * m) + 7)
        '''

        # Case 1: n is itself a perfect square => ans = 1
        if int(math.isqrt(n)) ** 2 == n:
            return 1

        # Case 2: sum of two squares; n = a^2 + b^2 for some integers a, b
        for i in range(1, int(math.isqrt(n)) + 1):
            remainder = n - i * i
            if int(math.isqrt(remainder)) ** 2 == remainder:
                return 2

        # Reduce n by removing factors of 4
        temp = n
        while temp % 4 == 0:
            temp //= 4

        # Case 3: Legendre's condition
        if temp % 8 == 7:
            return 4

        # Case 4: must be 3
        return 3

    def approach_4(self, n: int) -> int:
        '''
        Time Complexity = O(n * sqrt(n))
        Space Complexity = O(n)
        '''
        '''
        Approach : Optimize using precomputed squares
        '''

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        for s in range(1, n + 1):
            for sq in squares:
                if sq > s:
                    break
                dp[s] = min(dp[s], 1 + dp[s - sq])

        return dp[n]

    def approach_3(self, n: int) -> int:
        '''
        Time Complexity = O(n * (n^1/2))
        Space Complexity = O(n)
        '''
        '''
        Approach : Iterative DP : Bottom-Up

        Recurrence Relation :

        State Definition :
        dp(n) = minimum number of perfect squares that sum to n

        Base case :
        dp(0) = 0, minimum number of perfect squares that sum to zero = zero numbers

        Recurrence :
        dp(n) = 1 + min(dp(n - i^2)) for all i such that i^2 <= n

        => dp(n) = 1 + min(dp(n - 1^2), dp(n - 2^2), dp(n - 3^2), dp(n - 4^2) ...)

        dp[N] = answer

        Intuition :
        Choose one perfect square i^2
        That choice contributes 1
        The remaining sum is n - i^2
        Solve the remainder optimally
        Take the minimum over all valid squares

        Boundary Condition :
        dp(n) is defined only for n >= 0
        not allowed => dp(n − i^2) when n−i^2 < 0
        => 1 <= i^2 <= n

        Table of Variables :
        n = 12
        dp = [0, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')]

        i = 1, we construct every number using perfect square '1' only
        dp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        (1+1+1+1+1 = 5, to get 5)

        i = 2, perfect square = 4
                          | start
        dp = [0, 1, 2, 3, 1, 2, 3, 4, 2, 3, 4, 5, 3]
        (5 = 4+1)

        i = 3, perfect square = 9
                                         | start
        dp = [0, 1, 2, 3, 1, 2, 3, 4, 2, 1, 2, 3, 3]
        (12 = 4+4+1 or 9+1+1+1)
        '''
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for s in range(1, n + 1):
            i = 1
            while i * i <= s:
                sq = i * i
                dp[s] = min(dp[s], 1 + dp[s - sq])
                i += 1

        return dp[n]

    def approach_2(self, n: int) -> int:
        '''
        Time Complexity = O(n * (n^1/2))
        Space Complexity = O(n)
        '''
        '''
        Approach : Memoization : Top-Down
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
