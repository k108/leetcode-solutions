class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        return self.approach_1(nums)

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
