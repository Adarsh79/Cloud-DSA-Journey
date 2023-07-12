class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data


class CircularLinkList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        newNode = Node(data)
        if self.is_empty():
            newNode.next = newNode
            self.head = newNode
        else:
            current = self.head
            while current is not self.head:
                current = current.next
            current.next = newNode
            newNode.next = self.head

        return self.head

    def display(self):
        if self.is_empty():
            print("The circular linked list is empty")
        else:
            current = self.head
            while current is not self.head:
                print(current.data, end="")
                current = current.next


obj = CircularLinkList()
obj.append(20)
obj.append(2)
obj.append(3)
obj.append(4)
obj.append(5)
obj.display()
