class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def PrintQ(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

    def Enqueue(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.first = new_node
            self.last = new_node

        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def Dequeue(self):
        if self.length == 0:
            return None

        temp = self.first
        self.first = self.first.next
        temp.next = None

        if self.length == 0:
            self.last = None

        self.length -= 1

        return temp.value


# examples:
Q = Queue(3)
Q.Enqueue(2)
Q.Enqueue(2)
print(Q.Dequeue())
Q.PrintQ()
