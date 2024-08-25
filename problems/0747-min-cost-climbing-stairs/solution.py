class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Time Complexity : O(n)
        """
        cost.append(0)
        N = len(cost)

        # dp[i] is the minimum cost to climb to the top starting from the ith staircase
        for i in range(N -3, -1, -1):
            cost[i]+=min(cost[i+1], cost[i+2])
        
        return min(cost[0], cost[1])
        
