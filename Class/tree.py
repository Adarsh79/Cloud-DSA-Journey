from queue import Queue


class Node:
    def __init__(self, data):
        self.data = data
        self.list = []
        self.parent = None


class TreeNode:
    def create(self, data=int(input("Enter the root data: "))):
        root = None
        # data = int(input("Enter the Root data : "))

        if -1 != data:
            newNode = Node(data)
            root = newNode

        else:
            return root

        pendingNode = Queue()
        pendingNode.put(root)

        while pendingNode.qsize() > 0:
            front = pendingNode.get()
            n = int(input(f"How many Children do you want to enter? : {front.data} : "))
            if n > 0:
                for i in range(n):
                    data = int(input(f"Enter the children {front.data}'s data : "))
                    newNode = Node(data)
                    front.list.append(newNode)
                    pendingNode.put(newNode)
        return root


obj = TreeNode()
obj.create()
