class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Time Complexity : O(n)
        Space Complexity : O(n), extra stack used
        """
        max_area = 0
        stack = [] # pair : (index, height)
        for i, h in enumerate(heights):
            # start index of current height, as we do not know if we can extend backwards
            start = i
            while stack and stack[-1][1] > h:
                # stack is non-empty and height of stack top > current height
                # pop the stack
                # update max_area
                # extend current height backwards
                index, height = stack.pop()
                # width = current index - index where this height started at
                max_area = max(max_area, height * (i - index))
                # extend start index backwards to the index that we popped as, 
                # height of stack top > current height
                start = index
            
            # add start index extended backwards and not current index
            stack.append((start, h))
        
        # leftover entries in the stack, 
        # able to be extended all the ways to the end of histogram
        for i, h in stack:
            # width = length of the histogram - stored start value in the stack as,
            # these are extended all the ways to the end of histogram
            max_area = max(max_area, h * (len(heights) - i))
        
        return max_area


