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

    def __reverse(self, head, tail=None):
        if head is None:
            trav = {"first": None, "second": None}
            return trav
        temp = self.__reverse(head.next, tail)
        if temp["first"] is None:
            temp["first"] = head
            temp["second"] = head
        else:
            head.next = None
            temp["second"].next = head
            temp["second"] = head

        return temp

    def reverse(self):
        if self.head is None:
            return
        self.__reverse(self.head)
        self.display()
        print("\n")
        return temp["first"]


obj = LinkedListFunction()
obj.create()
obj.display()
obj.reverse()
