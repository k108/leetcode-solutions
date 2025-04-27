class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        # First turn the input into a set of numbers -> O(n)
        # Then we can ask in O(1) whether we have a certain number
        # Since we check each streak only once, this is overall O(n)
        # Avoids unnecessary backward scans

        # Using hashset
        nums = set(nums)
        lcs = 0
        for x in nums:
            # Number x is the start of a streak (i.e., x-1 is not in the set)
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                lcs = max(lcs, y - x)
        return lcs
