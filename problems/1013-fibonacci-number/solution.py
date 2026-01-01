class Solution:
    cache = {}

    def fib(self, n: int) -> int:
        '''
        Time Complexity : O(n)
        Space Complexity : O(1)
        '''
        '''
        Bottom-Up DP /
        Iterative DP
        '''
        if n <= 1:
            return n

        f_minus_2, f_minus_1 = 0, 1

        for _ in range(1, n):
            f = f_minus_2 + f_minus_1
            f_minus_2, f_minus_1 = f_minus_1, f

        return f_minus_1
