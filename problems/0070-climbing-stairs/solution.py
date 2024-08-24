class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def fibonacci(k):
            if k in cache:
                return cache[k]

            if k<=2:
                return 1
            else:
                result = fibonacci(k-1)+fibonacci(k-2)
                cache[k] = result
                return result
        
        return fibonacci(n+1)


        
