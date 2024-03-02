"""
Challenge: Implement Two Stacks Using One List

Implement the following functions to implement two stacks using a single array such that for storing elements both stacks should use the same array.
An illustration is also provided for your understanding.
Also, for this problem, initialize a Python list with the provided fixed size and perform all the operations in-place without growing or shrinking the list!

Prototypes:
def push1(value): # pushes value in stack 1
def push2(value): # pushes value in stack 2
def pop1(): # pops an element from stack 1
def pop2():# pops an element from stack 2

"""


# The meat:
class TwoStacks:

    # constructor
    def __init__(self, n):
        self.size = n
        # populating 0s on all n indices of array arr
        self.arr = [0] * n
        self.top1 = -1
        self.top2 = self.size

    # Method to push an element x to stack1
    def push1(self, x):

        # There is at least one empty space for new element
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = x

        else:
            print("Stack Overflow ")
            exit(1)

    # Method to push an element x to stack2
    def push2(self, x):

        # There is at least one empty space for new element
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = x

        else:
            print("Stack Overflow ")
            exit(1)

    # Method to pop an element from first stack
    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 -= 1
            return x
        else:
            print("Stack Underflow ")
            exit(1)

    # Method to pop an element from second stack
    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 += 1
            return x
        else:
            print("Stack Underflow ")
            exit()


if __name__ == "__main__":
    stack = TwoStacks(10)
    stack.push1(20)
    stack.push2(10)
    print(stack.pop1())
    stack.push1(100)
    print(stack.pop2())