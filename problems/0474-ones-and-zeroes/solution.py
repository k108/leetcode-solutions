class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        return self.approach_2(strs, m, n)

    def approach_2(self, strs: List[str], m: int, n: int) -> int:
        '''
        Time Complexity : O(n^2)
        Space Complexity : O(n)
        '''
        '''
        Appoach : Memoization / Knapsack 0/1
        Capacity : at most m 0's and n 1's
        Weight : m 0's and n 1's
        Profit : largest subset
        '''
        @cache
        def dfs(i, capacity):
            if i == len(strs):
                return 0

            # Skip item i
            max_profit = dfs(i + 1, capacity)

            # Include item i
            new_capacity = (capacity[0] - strs[i].count('0'), capacity[1] - strs[i].count('1'))
            if new_capacity[0] >= 0 and new_capacity[1] >= 0:
                p = 1 + dfs(i + 1, new_capacity)
                # Compute the max
                max_profit = max(max_profit, p)

            return max_profit
        
        return dfs(0, (m,n))

    def approach_1(self, strs: List[str], m: int, n: int) -> int:
        '''
        Time Complexity : O(2^n)
        Space Complexity : O(n)
        '''
        '''
        Appoach : DFS / Knapsack 0/1
        Capacity : at most m 0's and n 1's
        Weight : m 0's and n 1's
        Profit : largest subset
        '''
        def dfs(i, capacity):
            if i == len(strs):
                return 0

            # Skip item i
            max_profit = dfs(i + 1, capacity)

            # Include item i
            new_capacity = (capacity[0] - strs[i].count('0'), capacity[1] - strs[i].count('1'))
            if new_capacity[0] >= 0 and new_capacity[1] >= 0:
                p = 1 + dfs(i + 1, new_capacity)
                # Compute the max
                max_profit = max(max_profit, p)

            return max_profit
        
        return dfs(0, (m,n))
