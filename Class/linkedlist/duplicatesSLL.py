class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data


class LinkedListFunction:
    def __init__(self):
        self.head = None
        self.tail = None

    def create(self):
        datas = int(input("Enter the data : "))
        while datas != -1:
            if self.head is None:
                self.head = Node(datas)
                self.tail = self.head
            else:
                newNode = Node(datas)
                self.tail.next = newNode
                self.tail = self.tail.next
            datas = int(input("Enter the data : "))
        return self.head

    def display(self, head):
        if head is None:
            return
        print(head.data, " ", end="")
        self.display(head.next)

    def remove_duplicate(self):
        trav = self.head

        while trav is not None and trav.next is not None:
            tail = trav

            while tail.next is not None:
                if trav.data == tail.next.data:
                    tail.next = tail.next.next
                else:
                    tail = tail.next

            trav = trav.next


obj = LinkedListFunction()
newHead = obj.create()
obj.remove_duplicate()
obj.display(newHead)
