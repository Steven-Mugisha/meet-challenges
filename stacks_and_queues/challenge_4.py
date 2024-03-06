""""
    Challenge: Implement a Queue Using Stacks.
    Problem Statement: You have to implement the enqueue() and dequeue() functions using the MyStack class we created earlier. enqueue( ) will insert a value into the queue and dequeue( ) will remove a value from the queue.

    Input:
    enqueue( ): A value to insert into the queue

    dequeue( ): Does not require any input

    Output:
    enqueue( ): Does not return anything

    dequeue( ): Pops out and returns the oldest value in the queue

    Sample Input:
        value = 5 # [1, 2, 3, 4]
        enqueue(value)
        dequeue()

    Sample Output
        True # [1, 2, 3, 4, 5]
        1 # [2, 3, 4, 5]

N.B feel free to write your own Stack or Queue classes or use the ones provided below.
"""

# The meat:
# We can use 2 stacks for this purpose,main_stack to store original values
# and temp_stack which will help in enqueue operation.
# Main thing is to put first entered element at the top of main_stack


class NewQueue:
    # Can use size from argument to create stack
    def __init__(self):
        self.main_stack = MyStack()
        self.temp_stack = MyStack()

    # Inserts Element in the Queue
    def enqueue(self, value):
        # Push the value into main_stack in O(1)
        if self.main_stack.is_empty() and self.temp_stack.is_empty():
            self.main_stack.push(value)
            print(str(value) + "init main enqueued")
        else:
            while not self.main_stack.is_empty():
                self.temp_stack.push(self.main_stack.pop())
            # inserting the value in the queue
            self.main_stack.push(value)
            print(str(value) + "temp enqueued")
            while not self.temp_stack.is_empty():
                self.main_stack.push(self.temp_stack.pop())

    # Removes Element From Queue
    def dequeue(self):
        # If stack empty then return None
        if self.main_stack.is_empty():
            return None
        value = self.main_stack.pop()
        print(str(value) + "main dequeued")
        return value


# Stack:
class MyStack:
    def __init__(self):
        self.stack_list = []
        self.stack_size = 0

    def is_empty(self):
        return self.stack_size == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return self.stack_size

    def push(self, value):
        self.stack_size += 1
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        self.stack_size -= 1
        return self.stack_list.pop()


if __name__ == "__main__":
    queue = NewQueue()
    for i in range(5):
        queue.enqueue(i + 1)
    print("----------")
    for i in range(5):
        queue.dequeue()
