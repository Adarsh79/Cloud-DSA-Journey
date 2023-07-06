# class Node:
#     data = None
#     next = None
#
#     def __init__(self, data):
#         self.data = data
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def create(self):
#         data = int(input("Enter the data: "))
#         while data != -1:
#             if self.head is None:
#                 self.head = self.tail = Node(data)
#             else:
#                 newNode = Node(data)
#                 self.tail.next = newNode
#                 self.tail = self.tail.next
#             data = int(input("Enter the data: "))
#         return self.head
#
#     def print(self):
#         if self.head is None:
#             return
#         while self.head:
#             print(self.head.data, " ", end="")
#             self.head = self.head.next
#
#     def mid(self):
#         slow = fast = self.head
#         count = 0
#         while (fast is not None) and (fast.next is not None):
#             count += 1
#             slow = slow.next
#             fast = fast.next.next
#         return {"address": slow, "index": count}
#
#     def new_linkedlist(self):
#         temp = self.head
#         comparison = Node(temp.data)
#         mid = self.mid()
#         while temp.next is not mid["address"]:
#             comparison.data = temp.data
#             comparison = comparison.next
#             temp = temp.next
#
#         # if comparison is None:
#         #     return
#         while comparison:
#             print(comparison.data, " ", end="")
#             comparison = comparison.next
#
#
#
# obj = LinkedList()
# obj.create()
# obj.new_linkedlist()


class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def create(self):
        data = int(input("Enter the data: "))
        while data != -1:
            if self.head is None:
                self.head = self.tail = Node(data)
            else:
                newNode = Node(data)
                self.tail.next = newNode
                self.tail = self.tail.next
            data = int(input("Enter the data: "))
        return self.head

    def print(self):
        if self.head is None:
            return
        while self.head:
            print(self.head.data, " ", end="")
            self.head = self.head.next

    def mid(self):
        slow = fast = self.head
        count = 0
        while (fast is not None) and (fast.next is not None):
            count += 1
            slow = slow.next
            fast = fast.next.next
        return {"address": slow, "index": count}

    def reverse(self):
        prev = None
        temp = self.head
        while temp is not None:
            trav = temp.next
            temp.next = prev
            prev = temp
            temp = trav
        self.head = prev

    def __is_palindrome(self, head, comp):
        if head is None:
            return True

        temp = self.__is_palindrome(head.next, comp.next)

        if temp:
            if comp.next is None:
                return True
            if head.data == comp.data:
                return True
            else:
                return False
        else:
            return False

    def is_palindrome(self):
        temp = self.head
        cur = comparison = Node(temp.data)
        mid = self.mid()
        while temp.next is not mid["address"]:
            comparison.data = temp.data
            comparison = comparison.next
            temp = temp.next

        return self.__is_palindrome(self.head, cur)


obj = LinkedList()
obj.create()
print(obj.is_palindrome())
