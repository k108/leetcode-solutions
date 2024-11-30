class StockSpanner:

    def __init__(self):
        """
        Time Complexity : O(n), as each element will be added or removed from stack atmost once 
        Space Complexity : O(n), as we are using extra stack
        """
        self.stack = [] # pair : (price, span)
        
    def next(self, price: int) -> int:
        span = 1
        # monotonically decreasing stack
        while self.stack and self.stack[-1][0] <= price:
            p, s = self.stack.pop()
            # we add pre-computed older spans, instead of re-computing them
            span += s
        self.stack.append((price, span))
        return span
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
