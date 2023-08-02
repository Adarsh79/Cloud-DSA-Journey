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


def __height(root):
    if not root:
        return 0

    return max(__height(root.left) + 1, __height(root.right) + 1)


def height(root):
    if not root:
        return True

    else:
        left = height(root.left)
        right = height(root.right)
        if left and right:
            if abs(__height(root.left) - __height(root.right)) <= 1:
                return True
            else:
                return False

        return False


newRoot = create()
display(newRoot)
print(height(newRoot))
