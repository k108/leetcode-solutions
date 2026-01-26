class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        return self.approach_5(nums)

    def approach_5(self, A: List[int]) -> bool:
        '''
        Time Complexity: O(N * target)
        Space Complexity: O(N * target)
        '''
        '''
        Approach:
        Bottom-up DP : Value-Based 0/1 - Knapsack

        0/1 Knapsack Recurrence Relation =>

        State Definition :
        Let dp[i][w] = maximum value achievable using the first i items
                    with knapsack capacity w

        Base Case:
        dp[0][w] = 0, for all w i.e. No items -> no value
        dp[i][0] = 0 , for all i i.e. Zero capacity -> no value

        Recurrence:
        If weight[i-1] <= w:
            dp[i][w] = max(
                dp[i-1][w],                          # exclude item i
                value[i-1] + dp[i-1][w - weight[i-1]]  # include item i
            )
        Else:
            dp[i][w] = dp[i-1][w]                    # cannot include item i

        Boundary Conditions:
        0 <= i <= n
        0 <= w <= capacity

        Each DP state represents the best (or possible) outcome using a prefix of items 
        and a fixed capacity, with the recurrence modeling the 
        choice to include or exclude the current item.

        We want to find subset of items that add up to target_sum
        Given : 'n' items ~ Knapsack items
        target_sum ~ target_sum capacity
        Task : Combination that sums upto target_sum exists or not
        But, for Knapsack, it is, Finding maximum value of Combination
        So, we modify the formula,

        dp[i][w] = dp[i-1][w] or dp[i-1][w-w_i]
        here,
        dp[i][w] -> If there is a combination out of first 'i' items, that sum upto 'w'
        dp[i-1][w] -> If there is a combination out of first 'i-1' items, that sum upto 'w', 
        and we ignore 'ith' item
        dp[i-1][w-wi] -> If there is a combination out of first 'i-1' items, that sum upto 'w-w_i', 
        and we include 'ith' item, i.e. by adding w_i, we get: (w-w_i) + w_i = w

        if w-w_i < 0, we do not consider the case of including 'ith' item
        dp[i-1][w-w_i]
        so automatically,
        dp[i][w] = dp[i-1][w]

        Base case:
        With 0 elements, we can always make sum = 0

        Subset Sum (0/1 Knapsack Decision Version) Recurrence Relation =>
        
        State Definition :
        dp[i][s] = True if we can form sum s using first i elements (i.e., nums[0] to nums[i-1])
        
        Base Case:
        dp[0][0] = True; Using 0 elements, we can always form sum 0
        dp[0][s>0] = False, for all s > 0; Using 0 elements, we cannot form any positive sum
        
        Recurrence:
        If nums[i-1] <= s:
            dp[i][s] = dp[i-1][s] or dp[i-1][s - nums[i-1]]
            # exclude current element OR include it once
        Else:
            dp[i][s] = dp[i-1][s]
            # cannot include current element since it exceeds sum s

        Boundary Conditions:
        0 <= i <= n            (number of elements)
        0 <= s <= target_sum  (knapsack capacity / target subset sum)
        '''
        total_sum = sum(A)
        if not total_sum % 2 == 0:
            return False
        
        target_sum = total_sum // 2

        # Create DP table
        # Rows: len(A) + 1 (0 elements -> all elements)
        # Cols: target + 1 (sum from 0 -> target)
        dp = [[False] * (target_sum + 1) for _ in range(len(A) + 1)]

        # Base case:
        # With 0 elements, we can always make sum = 0
        dp[0][0] = True

        # here i=0 bcz everything other column (sum) of this row
        # cannot be created with 0 elements
        for i in range(1, len(A) + 1):
            for w in range(0, target_sum + 1):
                # We know that i-1 >=0 so we do not need extra check for that
                if w - A[i - 1] >= 0:
                    dp[i][w] = dp[i - 1][w - A[i - 1]] or dp[i - 1][w]
                else:
                    dp[i][w] = dp[i - 1][w]

        return dp[len(A)][target_sum]

    def approach_4(self, nums: List[int]) -> bool:
        '''
        Time Complexity: O(N * target_sum)
        Space Complexity: O(N * target_sum)
        '''
        '''
        Approach:
        Memoization
        '''
        # For pruning
        nums.sort()

        total_sum = sum(nums)
        if not total_sum % 2 == 0:
            return False
        
        target_sum = total_sum // 2

        def dfs(remaining, i, dp):
            # Pruning
            if i == len(nums) or remaining < nums[i]:
                return False

            if (remaining, i) in dp:
                return dp[(remaining, i)]
            
            if remaining == nums[i]:
                dp[(remaining, i)] = True
                return dp[(remaining, i)]

            # include current index or exclude it
            dp[(remaining, i)] = dfs(remaining - nums[i], i+1, dp) or dfs(remaining, i+1, dp)
            return dp[(remaining, i)]
        
        return dfs(target_sum, 0, {})

    def approach_3(self, nums: List[int]) -> bool:
        '''
        Time Complexity: O(2^N), each element is include/exclude
        Space Complexity: O(N), recursion stack
        '''
        '''
        Approach:
        Backtracking / DFS
        '''
        # For pruning
        nums.sort()

        total_sum = sum(nums)
        if not total_sum % 2 == 0:
            return False
        
        target_sum = total_sum // 2

        def dfs(remaining, i):
            # Pruning
            if i == len(nums) or remaining < nums[i]:
                return False
            
            if remaining == nums[i]:
                return True

            # include current index or exclude it
            return dfs(remaining - nums[i], i+1) or dfs(remaining, i+1)
        
        return dfs(target_sum, 0)

    def approach_2(self, nums: List[int]) -> bool:
        '''
        Time Complexity: O(2^N), each element is include/exclude
        Space Complexity: O(N), recursion stack
        '''
        '''
        Approach:
        Backtracking / DFS
        '''
        total_sum = sum(nums)
        if not total_sum % 2 == 0:
            return False
        
        target_sum = total_sum // 2

        def dfs(curr_sum, i):
            if curr_sum == target_sum:
                return True

            if i == len(nums) or curr_sum > target_sum:
                return False

            # include current index or exclude it
            return dfs(curr_sum + nums[i], i+1) or dfs(curr_sum, i+1)
        
        return dfs(0, 0)

    def approach_1(self, nums: List[int]) -> bool:
        '''
        Time Complexity: O(N * target_sum)
        Space Complexity: O(target_sum)
        '''
        '''
        Approach:
        Dynamic Programming (Subset Sum / 0-1 Knapsack)

        s_1, s_2 are subset of A
        s_1 intersection s_2 = None
        s_1 union s_2 = A

        sum(s_1) = sum(s_2)
        sum(s_1) + sum(s_1) = sum(s_2) + sum(s_1) {Adding sum(s_1) on both sides}
        => 2 * sum(s_1) = sum(A)
        => sum(s_1) = sum(A)/2
        => Find a subset s_1, such that sum(s_1) = sum(A)/2
        So, sum(A) should be Even else there cannot be a solution i.e. sum(A) % 2 == 0

        We maintain a set of all reachable subset sums.
        For each number, we update reachable sums by adding the number.
        If target_sum becomes reachable, we return True early.
        '''

        total_sum = sum(nums)
        if not total_sum % 2 == 0:
            return False
        
        target_sum = total_sum // 2
        subset_sums = {0}
        for num in nums:
            for possible_sum in list(subset_sums):
                new_sum = possible_sum + num
                if new_sum == target_sum:
                    return True
                if new_sum < target_sum:
                    subset_sums.add(new_sum)
        
        return False
