class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        Time Complexity : O(n)
        Space Complexity : O(n)
        '''
        limit = len(nums) // 2
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
            if freq[num] > limit:
                return num
        return None
