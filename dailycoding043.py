"""
This problem was asked by Amazon.

Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack.
If there are no elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently.
If there are no elements in the stack, then it should throw an error or return null.

Each method should run in constant time.

solution:
Use two stacks. One of the stacks will act as the queue and the other stack will
hold the index of the max elements.
"""
class Stack:

    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.max_stack or val > self.stack[self.max_stack[-1]]:
            self.max_stack.append(len(self.stack) - 1)

    def pop(self):
        if not self.stack:
            return None
        if len(self.stack) - 1 == self.max_stack[-1]:
            self.max_stack.pop()
        return self.stack.pop()

    def max(self):
        if not self.stack:
            return None
        return self.stack[self.max_stack[-1]]
    

def run_test(tests, stack):
    result = True
    for m, v in tests:
        result &= (m == stack.max())
        result &= (v == stack.pop())
    return result

def main():

    s = Stack()
    s.push(10)
    s.push(4)
    s.push(1)
    s.push(2)
    s.push(11)
    s.push(5)
    s.push(7)
    s.push(9)
    s.push(8)

    tests = (
        (11, 8),
        (11, 9),
        (11, 7),
        (11, 5),
        (11, 11),
        (10, 2),
        (10, 1)
    )

    if run_test(tests, s):
        print("Passed")
    else:
        print("Failed")


if __name__ == '__main__':
    main()
