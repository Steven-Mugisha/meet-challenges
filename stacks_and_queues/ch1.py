""" Challenge: Generate Binary Numbers from 1 to n using a Queue:

Problem Statement:
Implement a function find_bin(n) which will generate a binary numbers from 1 to till n in the form of a string using a queue.

N.B: Feel free to use the Queue and Stack classes provided or use your own clases from scratch.

Example:
    input: 5 - fin_bin(5)
    output: ["1", "10", "11", "100", "101"]

"""

# The meat:
from queue import MyQueue
def find_bin(number):
    q = MyQueue()
    q.enqueue(1)
    ans = []

    for i in range(number):
        ans.append(str(q.dequeue()))
        s1 = ans[i] + "0"
        s2 = ans[i] + "1"
        q.enqueue(s1)
        q.enqueue(s2)

    return ans

print(find_bin(3))

"""
Follow up question toward mastery...

"""

# can you try to implement the above function using a queue implemented using a linked list:

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class Queue:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.first = new_node
#         self.last = new_node
#         self.length = 1

#     def PrintQ(self):
#         temp = self.first
#         while temp:
#             print(temp.value)
#             temp = temp.next

#     def Enqueue(self, value):
#         new_node = Node(value)

#         if self.length == 0:
#             self.first = new_node
#             self.last = new_node

#         else:
#             self.last.next = new_node
#             self.last = new_node
#         self.length += 1

#     def Dequeue(self):
#         if self.length == 0:
#             return None

#         temp = self.first
#         self.first = self.first.next
#         temp.next = None

#         if self.length == 0:
#             self.last = None

#         self.length -= 1

#         return temp.value

# # examples:
# MyQueue = Queue(3)
# MyQueue.Enqueue(2)
# MyQueue.Enqueue(2)
# print(MyQueue.Dequeue())
# MyQueue.PrintQ()
