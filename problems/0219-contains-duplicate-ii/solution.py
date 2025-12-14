class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        element_to_idx = {}
        for i in range(len(nums)):
            if nums[i] in element_to_idx and i - element_to_idx[nums[i]] <= k:
                return True
            element_to_idx[nums[i]] = i

        return False
