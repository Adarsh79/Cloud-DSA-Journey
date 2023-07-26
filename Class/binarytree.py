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


def searchBST(root, val):
    flag = False
    if not root:
        return False

    if root.data == val:
        return True

    leftSubtree = searchBST(root.left, val)

    if leftSubtree:
        flag = True

    rightSubtree = searchBST(root.right, val)

    if rightSubtree:
        flag = True

    return flag


rootNode = create()
if searchBST(rootNode, 8):
    print(True)
else:
    print(False)
