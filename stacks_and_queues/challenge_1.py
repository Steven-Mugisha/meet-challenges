"""
    Challenge: Generate Binary Numbers from 1 to n using a Queue:

    Problem Statement:
    Implement a function find_bin(n) which will generate a binary numbers from 1 to till n in the form of a string using a queue.

    N.B: Feel free to use the Queue class provided down below or use your own clases from scratch.

    Example 1:
    Input: 6 - find_bin(6)
    Output: ["1", "10", "11", "100", "101", "110"]

    Example 2:
    Input: 10 - find_bin(10)
    Output: ["1", "10", "11", "100", "101", "110", "111", "1000", "1001", "1010"]

    Example 3:
    Input: 15 - find_bin(15)
    Output: ["1", "10", "11", "100", "101", "110", "111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"]

N.B feel free to write your own Stack or Queue classes or use the ones provided below
"""

# The meat:
def find_bin(number):
    q = MyQueue()
    q.enqueue(1)
    ans = []

    for i in range(number):
        ans.append(str(q.dequeue()))
        q.enqueue(ans[i] + "0")
        q.enqueue(ans[i] + "1")

    return ans


print(find_bin(3))

"""
    Follow up question toward mastery..!

    Can you try to implement the function fin_bin(value: int) -> List[str]
    while utilizing a queue build using a linked list. For reference look for an example under "queue.py" file.

"""


# queue class
class MyQueue:
    def __init__(self):
        self.queue_list = []
        self.queue_size = 0

    def is_empty(self):
        return self.queue_size == 0

    def front(self):
        if self.is_empty():
            return None
        return self.queue_list[0]

    def rear(self):
        if self.is_empty():
            return None
        return self.queue_list[-1]

    def size(self):
        return self.queue_size

    def enqueue(self, value):
        self.queue_size += 1
        self.queue_list.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        front = self.front()
        self.queue_list.remove(self.front())
        self.queue_size -= 1
        return front
