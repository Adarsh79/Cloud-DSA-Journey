from queue import Queue


class Node:
    def __init__(self, data):
        self.data = data
        self.child = []


def create(data=int(input("Enter the root data: "))):
    rootNode = None

    if -1 != data:
        newNode = Node(data)
        rootNode = newNode

    else:
        return rootNode

    pendingNode = Queue()
    pendingNode.put(rootNode)

    while pendingNode.qsize() > 0:
        front = pendingNode.get()
        n = int(input(f"How many Children do you want to enter? : {front.data} : "))
        if n > 0:
            for i in range(n):
                data = int(input(f"Enter the children {front.data}'s data : "))
                newNode = Node(data)
                front.child.append(newNode)
                pendingNode.put(newNode)
    return rootNode


def sum_nodes(root_node):
    Sum = 0

    if root_node is None:
        return 0

    q = [root_node]

    while len(q) != 0:
        n = len(q)

        while n > 0:
            p = q[0]
            q.pop(0)
            Sum += p.data

            for i in range(len(p.child)):
                q.append(p.child[i])
            n -= 1
    return Sum


newNode = create()
print(sum_nodes(newNode))
