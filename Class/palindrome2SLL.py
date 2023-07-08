class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Creation of linked list
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

    # Function to print the original linked list
    def print(self):
        self.__helper_print(self.head)

    def __helper_print(self, temp):
        if temp is None:
            return
        print(temp.data, "|", end="")
        self.__helper_print(temp.next)

    # Function to print the half linked list
    def display_sub_ll(self, comp):
        self.__helper_print(comp)

    # Function to find the address and index of the mid-element of a linked list
    def mid(self):
        slow = fast = self.head
        count = 0
        while (fast is not None) and (fast.next is not None):
            count += 1
            slow = slow.next
            fast = fast.next.next
        return {"address": slow, "index": count}

    # Function to reverse the inputted linked list
    def reverse(self, main_head=None):
        prev = None
        if main_head is None:
            temp = self.head
        else:
            temp = main_head
        while temp is not None:
            trav = temp.next
            temp.next = prev
            prev = temp
            temp = trav
        if main_head is None:
            self.head = prev
            return
        return prev

    def __is_palindrome(self, head, comp):
        if head is None:
            return True

        if head:
            if comp.next is None:
                return True
            if head.data == comp.data:
                return True
            else:
                return False
        else:
            return False

    # Function to check if the linked list is palindrome or not
    def is_palindrome(self):
        temp = self.head
        head2 = comparison = Node(temp.data)
        mid = self.mid()
        temp = temp.next

        while temp is not mid["address"].next:
            newNode = Node(temp.data)
            comparison.next = newNode
            comparison = comparison.next
            temp = temp.next

        head2 = self.reverse(head2)

        self.display_sub_ll(head2)

        return self.__is_palindrome(temp, head2)


obj = LinkedList()
obj.create()
print(obj.is_palindrome())
