from bst import *


def insert(root, value):
    if root is None:
        newNode = Node(value)
        root = newNode
        return root

    if value < root.val:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root


def update(root, key, value):
    if not root:
        return root

    if root.val == key:
        root.val = value

    if key < root.val:
        root.left = update(root.left, key, value)
    else:
        root.right = update(root.right, key, value)

    return root


nodes = [3, 2, -1, -1, 7, 4, -1, -1, 8, -1, -1]
nodes.reverse()
rootNode = create(nodes)
print("\n")

update(rootNode, 4, 1)
display(rootNode)
