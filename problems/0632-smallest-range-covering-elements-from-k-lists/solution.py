import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        '''
        Time Complexity : O(n* log k), where 'n' is total elements
        Space Complexity : O(k)
        '''

        '''
        Two pointer approach : 
        Take the smallest (take minimum) and keep shifting to right in that sorted array
        and keep recomputing the range
        '''

        # finding min among 'k' elements : O(n*k) -> O(n log k)
        min_heap = [] # (value, row, col)
        cur_max = float('-inf')

        # Step 1: Initialize heap with the first element (min) of each list
        for i in range(len(nums)):
            # heap element : {(value, idx of list, idx of val within that list)}
            heapq.heappush(min_heap, (nums[i][0], i, 0)) 
            cur_max = max(cur_max, nums[i][0])

        min_range = [float('-inf'), float('inf')]
        # Step 2: Two pointer approach
        while min_heap:
            cur_min, list_idx, i = heapq.heappop(min_heap)

            # Update the smallest range found so far
            if cur_max - cur_min < min_range[1] - min_range[0]:
                min_range = [cur_min, cur_max]
            
            # Add the next element from the same sorted list
            # to shrink the existing range 
            # best we can do is select the list with minimum
            # and move to its next element
            # there is no point of selecting the list with maximum
            # and moving to its next element
            if i + 1 < len(nums[list_idx]):
                nxt = nums[list_idx][i + 1]
                # Add the next element from the same list
                heapq.heappush(min_heap, (nxt, list_idx, i+1))
                # Adding an element could have increased cur_max
                cur_max = max(cur_max, nxt)
            else:
                # If we have exhausted any list, we stop
                break

        return min_range
        
