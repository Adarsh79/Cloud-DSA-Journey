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

    def __display(self, head):
        if head is None:
            return
        print(head.data, " ", end="")
        self.__display(head.next)

    def display(self):
        temp = self.head
        self.__display(temp)

    def reverse(self):
        prev = None
        temp = self.head
        while temp is not None:
            trav = temp.next
            temp.next = prev
            prev = temp
            temp = trav
        self.head = prev


obj = LinkedListFunction()
obj.create()
obj.reverse()
obj.display()
