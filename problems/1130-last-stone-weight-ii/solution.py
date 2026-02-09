class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        return self.approach_4(stones)

    def approach_4(self, stones: List[int]) -> int:
        '''
        Time Complexity : O(N * total_sum)
        Space Complexity : O(N * total_sum)
        '''
        '''
        Approach : Iterative DP

        Minimum subset sum difference problem
        '''
        N = len(stones)
        total_sum = sum(stones)

        dp = [[False] * (total_sum + 1) for _ in range(N + 1)]

        # Base case
        for i in range(N + 1):
            dp[i][0] = True

        # DP transition
        for i in range(1, N + 1):
            for j in range(total_sum + 1):
                if stones[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - stones[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]

        # Find closest sum to total_sum // 2
        for s in range(total_sum // 2, -1, -1):
            if dp[N][s]:
                return total_sum - 2 * s

    def approach_3(self, stones: List[int]) -> int:
        '''
        Approach : Memoization
        '''
        '''
        Partition an array into 2 subsets whose difference is minimal,
        S1 + S2  = S
        S1 - S2 = diff  

        => diff = S - 2 * S2  => minimize diff equals to maximize S2

        => Find the maximum of S2, range from 0 to S / 2

        dp[i][j]   = {true if some subset from 1st to j'th has a sum equal to sum i, false otherwise}
            i ranges from (sum of all elements) {1..n}
            j ranges from  {1..n}
        '''
        N = len(stones)
        dp = [[-1] * (3000 + 1) for _ in range(30 + 1)]

        def dfs(i, s_1, s_2):
            if i == N:
                return abs(s_1-s_2)

            if dp[i][s_1] != -1:
                return dp[i][s_1]
            
            dp[i][s_1] = min(dfs(i+1, s_1 + stones[i], s_2), dfs(i+1, s_1, s_2 + stones[i]))
            return dp[i][s_1]
        
        return dfs(0, 0, 0)

    def approach_2(self, stones: List[int]) -> int:
        '''
        Approach : Memoization
        '''
        N = len(stones)
        dp = [[-1] * (3000 + 1) for _ in range(30 + 1)]

        def dfs(i, difference):
            if i == N:
                if difference < 0:
                    return float('inf')
                else:
                    return difference
            if difference > 0 and dp[i][difference] != -1:
                return dp[i][difference]
            
            result = min(dfs(i+1, difference + stones[i]), dfs(i+1, difference - stones[i]))
            if difference > 0:
                dp[i][difference] = result
            return result
        
        return dfs(0, 0)

    def approach_1(self, stones: List[int]) -> int:
        '''
        Approach : DFS
        For every element we have 2 choices, whether to give it "+" sign or "-" sign,
        as we can either add that elemnt or subtract it.
        Then we find out by which path we get the minimum answer,
        as we want total sum to be as least as possible
        So once we cover all elements we check what is the sum:
        => if negative: not possible as remaining stone cannot have negative weight,
        so we return infinity
        => if positive: then we return whatever the curr_sum was, and then check
        from which sign we are getting minimum answer
        '''
        N = len(stones)

        def dfs(i, difference):
            if i == N:
                if difference < 0:
                    return float('inf')
                else:
                    return difference
            return min(dfs(i+1, difference + stones[i]), dfs(i+1, difference - stones[i]))
        
        return dfs(0, 0)
