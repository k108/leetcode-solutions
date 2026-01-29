class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        return self.approach_5(nums, target)

    def approach_5(self, nums: List[int], target: int) -> int:
        '''
        Time Complexity : O(N * target), the outer loop runs target times, and for each iteration,
        we potentially check all N numbers in nums

        Space Complexity : O(target), The array dp will have target + 1 elements, 
        each requiring constant space. 
        So the overall space complexity is linear in terms of the target value.
        '''
        '''
        Dynamic Programming : Top-Down (Memoization)
        '''

        dp = [-1]*(target + 1)
        dp[0] = 1

        def dfs(nums, target):
            if dp[target] != -1:
                return dp[target]
            
            result = 0

            for i in range(len(nums)):
                if target >= nums[i]:
                    result += dfs(nums, target - nums[i])

            dp[target] = result
            return result

        return dfs(nums, target)

    def approach_4(self, nums: List[int], target: int) -> int:
        '''
        Time Complexity: O(N * target)
        Space Complexity: O(target)
        '''
        @cache
        def dfs(t):
            if t == 0: return 1
            return sum(dfs(t-x) for x in nums if x <= t)
        return dfs(target)

    def approach_3(self, nums: List[int], target: int) -> int:
        '''
        Time Complexity : O(N * target), the outer loop runs target times, and for each iteration,
        we potentially check all N numbers in nums

        Space Complexity : O(target), The array dp will have target + 1 elements, 
        each requiring constant space. 
        So the overall space complexity is linear in terms of the target value.
        '''
        '''
        Dynamic Programming : Bottom-Up

        State Definition :
        dp(t) =  # combinatons that sum up to t

        Base Case :
        i=0; dp(0)=1
        Only one way to make 0 target = 1; i.e. choose nothing
        dp(target) -> Answer

        Recurrence Relation :
        dp(t) = Σ dp(t - x) for all x ∈ nums where x ≤ t
        
        Boundary Condition :

        Table of Variables :
        i=0; dp(0) = 1
        i=1; dp(1) = dp(0) = 1
        i=2; dp(2) = dp(1) + dp(0) = 2
        i=3; dp(3) = dp(2) + dp(1) + dp(0) = 4
        i=4; dp(3) + dp(2) + dp(1) = 7
        '''

        dp = [0] * (target+1)
        dp[0] = 1

        nums.sort()

        for t in range(1, target + 1):
            for num in nums:
                # if t >= num:
                #     dp[t] += dp[t - num]
                if num > t:
                    break

                dp[t] += dp[t - num]
        
        return dp[target]

    def approach_2(self, nums: List[int], target: int) -> int:
        '''
        Time Complexity : O(N * target), each unique target value is calculated once.
        For each calculation, we might iterate over all N numbers in nums.
        Space Complexity : O(target)
        '''
        '''
        Top-Down : Memoization
        '''
        nums.sort()
        dp = {}

        def dfs(target):
            if target in dp:
                return dp[target]

            if target == 0:
                return 1
            # Pruning
            # Given that nums is sorted, this means no combination can be formed
            # to achieve the current target. So, we immediately return 0, optimizing our recursion.
            if target < nums[0]:
                return 0
            
            result = 0

            for num in nums:
                # if target >= num:
                #     result += dfs(target - num)
                if target < num:
                    break
                result += dfs(target - num)
            
            dp[target] = result
            return result

        return dfs(target)

    def approach_1(self, nums: List[int], target: int) -> int:
        '''
        Time Complexity : O(N^target)
        Space Complexity : O(target)
        '''
        nums.sort()

        def dfs(target):
            if target == 0:
                return 1
            # Pruning
            # Given that nums is sorted, this means no combination can be formed
            # to achieve the current target. So, we immediately return 0, optimizing our recursion.
            if target < nums[0]:
                return 0
            
            result = 0

            for num in nums:
                # if target >= num:
                #     result += dfs(target - num)
                if target < num:
                    break
                result += dfs(target - num)
            
            return result

        return dfs(target)
