class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        Time Complexity : O(n*log(n))
        Time Complexity : O(1)
        '''

        '''
        Approaches ->

        1. Floyd's Cycle Detection (Fast-Slow Pointers): Treat the array as a linked list 
        to find a cycle.

        2. Binary Search: Count the numbers less than or equal to the middle element 
        to find the duplicate.

        Pigeonhole principle : if there are more items than containers, 
        then at least one container must contain more than one item.
        so as array is [1, n], if 5 is mid, then there should be 5 elements <= 5, if not then we look in [1, mid]; else we search in [mid+1, high]
        '''

        low = 1
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            count = 0
            for e in nums:
                if e<=mid:
                    count+=1
            # there are count elements greater than mid, so ans is in [1, mid]
            if count > mid:
                high=mid
            # there are count elements less than equal to mid, so ans is in [mid+1, high]
            else:
                low=mid+1

        return low




        


        
        







        
        
