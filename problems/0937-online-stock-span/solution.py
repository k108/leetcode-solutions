class Stack:
    def __init__(self):
        self.items = []
         
    # method for pushing an item on a stack
    def push(self, item):
        self.items.append(item)
         
    # method for popping an item from a stack
    def pop(self):
        return self.items.pop()
     
    # method to check whether the stack is empty or not
    def isEmpty(self):
        return (self.items == [])
     
    # method to get the top of the stack
    def peek(self):
        return self.items[-1]
     
    def __str__(self):
        return str(self.items)

class StockSpanner:

    def __init__(self):
        self.D = Stack()
        self.S = []
        self.A = []
        self.i = 0
        

    def next(self, price: int) -> int:
        self.A.append(price)
        self.S.append(None)
        # for i in range (0, len(self.A)):
        while not self.D.isEmpty() and self.A[self.i] >= self.A[self.D.peek()]:
                self.D.pop()
        if self.D.isEmpty():
            P = -1
        else:
            P = self.D.peek()
        self.S[self.i] = self.i - P
        self.D.push(self.i)
        self.i+=1
        return self.S[-1]
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
