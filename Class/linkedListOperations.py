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

        print(head.data, " ", end=" ")
        self.display(head.next)

    def delete(self):
        temp = self.head
        if temp is not None:
            self.head = temp.next
            temp.next = None
            del temp
            return self.head

    def search(self, key):
        temp = self.head
        idx = -1

        while temp is not None:
            if temp.data == key:
                idx += 1
                return "Element found at " + str(idx)
            idx += 1
            temp = temp.next

        return "\nElement not found!"


obj = LinkedListFunction()
newHead = obj.create()
obj.display(newHead)

# obj.delete()
# newHead = obj.head
# print("\nThe List after deletion: ")
# obj.display(newHead)

print(obj.search(23))
