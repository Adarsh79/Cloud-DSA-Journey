class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def create(root, item):
    if root is None:
        return Node(item)
    else:
        if root.val == item:
            return root
        elif root.val < item:
            root.right = create(root.right, item)
        else:
            root.left = create(root.left, item)

    return root


def display(root):
    if root is None:
        return

    print(root.val, end="|")

    display(root.left)
    display(root.right)


rootNode = insert()
display(rootNode)
# Updation of value