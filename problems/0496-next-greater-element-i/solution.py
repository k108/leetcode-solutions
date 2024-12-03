class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Time Complexity : O(m+n)
        Space Complexity : O(m)
        """
        # a greater element is greater than all numbers preceding it
        # we create a monotonically decreasing stack
        # if we encounter a greater number, we pop till it is greater and push it
        mono_inc_stack = []
        next_greater_map = {}
        for e in nums2:
            while mono_inc_stack and mono_inc_stack[-1]<e:
                next_greater_map[mono_inc_stack.pop()]=e
            mono_inc_stack.append(e)
        return [next_greater_map.get(e,-1) for e in nums1]


        
