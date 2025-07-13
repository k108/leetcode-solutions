class Node:
    def __init__(self, interval_start, interval_end):
        self.interval_start = interval_start
        self.interval_end = interval_end
        self.left = None
        self.right = None

    def insert(self, interval_start, interval_end):
        if interval_start >= self.interval_end:
            # start of new interval is greater than, end of current interval
            # new interval comes after, current interval
            # go to right
            # equal is allowed as "end" is not part of the interval
            if not self.right:
                self.right = Node(interval_start, interval_end)
                return True
            else:
                return self.right.insert(interval_start, interval_end)
        elif interval_end <= self.interval_start:
            # end of new interval is less than, start of current interval
            # new interval comes before, current interval
            # go to left
            # equal is allowed as "end" is not part of the interval
            if not self.left:
                self.left = Node(interval_start, interval_end)
                return True
            else:
                return self.left.insert(interval_start, interval_end)
        else:
            # overlap with current interval
            return False


class IntervalTree:
    def __init__(self):
        self.root = None
    
    # def insert(self, interval_start, interval_end):
    #     curr = self.root
    #     while True:
    #         if interval_start >= curr.interval_end:
    #             # start of new interval is greater than, end of current interval
    #             # new interval comes after, current interval
    #             if not curr.right:
    #                 curr.right = Node(interval_start, interval_end)
    #                 return True
    #             curr = curr.right
    #         elif interval_end <= curr.interval_start:
    #             # end of new interval is less than, start of current interval
    #             # new interval comes before, current interval
    #             if not curr.left:
    #                 curr.left = Node(interval_start, interval_end)
    #                 return True
    #             curr = curr.left
    #         else:
    #             # overlap with current interval
    #             return False
    # def insert(self, interval_start, interval_end, curr):
    #     if interval_start >= curr.interval_end:
    #         # start of new interval is greater than, end of current interval
    #         # new interval comes after, current interval
    #         # go to right
    #         # equal is allowed as "end" is not part of the interval
    #         if not curr.right:
    #             curr.right = Node(interval_start, interval_end)
    #             return True
    #         else:
    #             return self.insert(interval_start, interval_end, curr.right)
    #     elif interval_end <= curr.interval_start:
    #         # end of new interval is less than, start of current interval
    #         # new interval comes before, current interval
    #         # go to left
    #         # equal is allowed as "end" is not part of the interval
    #         if not curr.left:
    #             curr.left = Node(interval_start, interval_end)
    #             return True
    #         else:
    #             return self.insert(interval_start, interval_end, curr.left)
    #     else:
    #         # overlap with current interval
    #         return False
    def insert(self, interval_start, interval_end):
        if not self.root:
            self.root = Node(interval_start, interval_end)
            return True
        else:
            return self.root.insert(interval_start, interval_end)


class MyCalendar:

    def __init__(self):
        self.interval_tree = None

    def book(self, startTime: int, endTime: int) -> bool:
        '''
        Time Complexity : O(n log n)
        Space Complexity : O(n)
        '''
        if not self.interval_tree:
            self.interval_tree = IntervalTree()
        return self.interval_tree.insert(startTime, endTime)

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
