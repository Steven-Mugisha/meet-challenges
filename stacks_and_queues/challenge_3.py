"""
    Challenge: Reversing First k Elements of Queue.
    Problem statement: Implement the function reverseK(queue, k) which takes a queue and a number “k” as input and reverses the first “k” elements of the queue.
    Output: The queue with first “k” elements reversed. Remember to return the queue itself!

    Example:
    Queue = [1,2,3,4,5,6,7,8,9,10], k = 5
    Result:
    Queue = [5,4,3,2,1,6,7,8,9,10]

N.B feel free to write your own Stack or Queue classes or use the ones provided below
"""

# The meat:
# 1.Push first k elements in queue in a stack.
# 2.Pop Stack elements and enqueue them at the end of queue
# 3.Dequeue queue elements till "k" and append them at the end of queue


def reverseK(queue, k):
    # Handling invalid input
    if queue.is_empty() is True or k > queue.size() or k < 0:
        return None

    stack = MyStack()
    for i in range(k):
        stack.push(queue.dequeue())
    while stack.is_empty() is False:
        queue.enqueue(stack.pop())
    size = queue.size()
    for i in range(size - k):
        queue.enqueue(queue.dequeue())

    return queue


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


# Queue:
class MyQueue:
    def __init__(self):
        self.items = DoublyLinkedList()

    def is_empty(self):
        return self.items.length == 0

    def front(self):
        if self.is_empty():
            return None
        return self.items.get_head()

    def rear(self):
        if self.is_empty():
            return None
        return self.items.tail_node()

    def size(self):
        return self.items.length

    def enqueue(self, value):
        return self.items.insert_tail(value)

    def dequeue(self):
        return self.items.remove_head()

    def display(self):
        return self.items.__str__()


# DoublyLinkedList:
class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None
        self.previous_element = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get_head(self):
        if self.head != None:
            return self.head.data
        else:
            return False

    def is_empty(self):
        if self.head is None:  # Check whether the head is None
            return True
        else:
            return False

    def insert_tail(self, element):
        temp_node = Node(element)
        if self.is_empty():
            self.head = temp_node
            self.tail = temp_node
        else:
            self.tail.next_element = temp_node
            temp_node.previous_element = self.tail
            self.tail = temp_node
        self.length += 1
        return temp_node.data

    def remove_head(self):
        if self.is_empty():
            return False
        nodeToRemove = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = nodeToRemove.next_element
            self.head.previous_element = None
            nodeToRemove.next_element = None
        self.length -= 1
        return nodeToRemove.data

    def tail_node(self):
        if self.head != None:
            return self.tail.data
        else:
            return False

    def __str__(self):
        val = ""
        if self.is_empty():
            return ""
        else:
            temp = self.head
            val = "[" + str(temp.data) + ", "
            temp = temp.next_element

            while temp.next_element:
                val = val + str(temp.data) + ", "
                temp = temp.next_element
            val = val + str(temp.data) + "]"
        return val


if __name__ == "__main__":
    # testing our logic
    queue = MyQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    queue.enqueue(8)
    queue.enqueue(9)
    queue.enqueue(10)
    print("the queue before reversing:")
    print(queue.items)
    reverseK(queue, 10)
    print("the queue after reversing:")
    print(queue.items)
