# Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.nextAdd = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.temp = None


obj = LinkedList()

obj.head = n1 = Node(1)
n2 = Node(2)
n1.nextAdd = n2
n3 = Node(3)
n2.nextAdd = n3


obj.temp = obj.head
while obj.temp is not None:
    print(obj.temp.data)
    obj.temp = obj.temp.nextAdd
