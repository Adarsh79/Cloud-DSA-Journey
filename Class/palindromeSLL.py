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

    def __is_palindrome(self, head, arr):
        if head is None:
            return True
        temp = self.__is_palindrome(head.next, arr)
        if temp:
            if not arr:
                return True
            if head.data == arr.pop():
                return True
            else:
                return False
        else:
            return False

    def is_palindrome(self):
        prev = temp = self.head
        arr = []
        mid = self.mid()
        for i in range(mid["index"] + 1):
            arr.append(temp.data)
            temp = temp.next

        i = 0
        n = len(arr) - 1

        while i < n:
            arr[i], arr[n] = arr[n], arr[i]
            i += 1
            n -= 1
        return self.__is_palindrome(prev, arr)


obj = LinkedList()
obj.create()
print(obj.is_palindrome())
