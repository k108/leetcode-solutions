class Node:
    def __init__(self, data, min_val):
        self.data=data
        # Consider each node in the stack having a minimum value
        # Minimum value from the bottom of the stack till this current element
        self.min_val=min_val

class MinStack:

    def __init__(self):
        self.arr = []
        

    def push(self, val: int) -> None:
        self.arr.append(Node(data=val, min_val=min(val, self.arr[-1].min_val if self.arr else val )))


    def pop(self) -> None:
        self.arr.pop()
        

    def top(self) -> int:
        return self.arr[-1].data
        

    def getMin(self) -> int:
        return self.arr[-1].min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
