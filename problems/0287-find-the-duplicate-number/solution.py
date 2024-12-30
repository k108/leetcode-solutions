class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        Time Complexity : O(n)
        Time Complexity : O(1)
        '''

        '''
        Approaches ->

        1. Floyd's Cycle Detection (Fast-Slow Pointers): Treat the array as a linked list to find a cycle.
        2. Binary Search: Count the numbers less than or equal to the middle element to find the duplicate.
        '''

        slow = nums[0]
        fast = nums[0]

        # detect cycle :
        # meeting point is not necessarily the duplicate number; 
        # it's just a point inside the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Find the Start of the Cycle
        # when both pointers move at the same speed, 
        # they will eventually meet at the starting point of the cycle

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
        


        
        







        
        
