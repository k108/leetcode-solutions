class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.num_overlap = 0
        self.left = None
        self.right = None
        self.lazy  = 0

class SegmentTree:
    def __init__(self, start, end):
        self.root = Node(start, end)
    
    def update(self, curr, update_start, update_end, val):
        if update_start > curr.end or update_end < curr.start:
            # no overlap
            return
        if update_start <= curr.start and update_end >= curr.end:
            # complete overlap
            curr.lazy += val
            return

        # partial overlap
        self.push_down(curr)

        mid = (curr.start + curr.end) // 2
        if not curr.left:
            curr.left = Node(curr.start, mid)
        if not curr.right:
            curr.right = Node(mid + 1, curr.end)

        self.update(curr.left, update_start, update_end, val)
        self.update(curr.right, update_start, update_end, val)
        curr.num_overlap = max(curr.left.num_overlap + curr.left.lazy, curr.right.num_overlap + curr.right.lazy)

    def max_num_overlap(self, curr, query_start, query_end):
        '''
        Time Complexity : O(log 10^9)
        Space Complexity : O(n log R) → O(n), n = num_bookings
        '''
        if query_start > curr.end or query_end < curr.start:
            # no overlap
            return 0
        if query_start <= curr.start and query_end >= curr.end:
            # complete overlap
            return curr.num_overlap + curr.lazy
        
        # partial overlap
        self.push_down(curr)

        mid = (curr.start + curr.end) // 2
        left_max = self.max_num_overlap(curr.left or Node(curr.start, mid), query_start, query_end)
        right_max = self.max_num_overlap(curr.right or Node(mid + 1, curr.end), query_start, query_end)
        return max(left_max, right_max)

    def push_down(self, curr):
        if curr.lazy:
            mid = (curr.start + curr.end) // 2

            if not curr.left:
                curr.left = Node(curr.start, mid)
            if not curr.right:
                curr.right = Node(mid + 1, curr.end)
            
            curr.left.lazy += curr.lazy
            curr.right.lazy += curr.lazy
            curr.num_overlap += curr.lazy
            curr.lazy = 0


class MyCalendarTwo:

    def __init__(self):
        self.seg_tree = SegmentTree(0, 10**9)
        

    def book(self, startTime: int, endTime: int) -> bool:
        endTime -= 1
        if self.seg_tree.max_num_overlap(self.seg_tree.root, startTime, endTime) == 2:
            return False
        self.seg_tree.update(self.seg_tree.root, startTime, endTime, 1)
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)
