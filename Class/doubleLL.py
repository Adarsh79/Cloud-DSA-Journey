class Node:
    prev = None
    data = None
    next = None

    def __init__(self, data):
        self.data = data


class LinkedListFunction:
    def __init__(self):
        self.head = None
        self.tail = None
