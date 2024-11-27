class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Time Complexity : O(n log(n))
        """
        pos_speed=[(pos,sp) for pos, sp in zip(position, speed)]
        
        # reverse sorted order
        pos_speed.sort(reverse=True)

        stack = []

        for pos, sp in pos_speed:
            curr_time = (target - pos)/sp
            stack.append(curr_time)
            # overtake only possible if more than 1 car present
            if len(stack)>=2  and stack[-1] <= stack[-2]:
            # Before or same time = Car fleet i.e. <= , faster overtakes slower 
            # and faster gets popped from stack 
            # as speed of the slower will be considered for car fleet,
            # also faster will be at top of the stack.
                stack.pop()

        # return number of car fleets
        return len(stack)
            

        
