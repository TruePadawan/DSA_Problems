"""
My attempt on implementing a different approach I got from another Leetcoder's solution
The idea is to just always store the min element with each element in the stack
Basically each element in the stack will be a tuple (actual value, min element)
"""


class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        min_val = self.getMin()
        if min_val is None or val < min_val:
            min_val = val
        self.stack.append((val, min_val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[-1][1]


# Initial Solution - Works Fine; Passed all Test Cases
# class MinStack:

#     def __init__(self):
#         self.stack = []
#         self.sorted_data = []

#     def push(self, val: int) -> None:
#         self.stack.insert(0, val)
#         self.sorted_data = sorted(self.stack)

#     def pop(self) -> None:
#         self.stack.pop(0)
#         self.sorted_data = sorted(self.stack)

#     def top(self) -> int:
#         return self.stack[0]

#     def getMin(self) -> int:
#         return self.sorted_data[0]
