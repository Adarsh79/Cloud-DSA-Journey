class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create():
    root = None
    data = int(input("Enter the root node: "))

    if data == -1:
        return root

    newNode = Node(data)
    root = newNode

    root.left = create()
    root.right = create()

    return root


def display(root):
    if root is None:
        return

    print(root.data, end="|")

    display(root.left)
    display(root.right)


rootNode = create()
display(rootNode)
