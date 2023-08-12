from bst import Node


def create():
    data = int(input("Enter the data: "))

    if data == -1:
        return None

    newNode = Node(data)
    root = newNode

    q = [root]

    while len(q) > 0:
        front = q.pop(0)

        data = int(input("Enter the data : "))
        if data == -1:
            return root
        newNode = Node(data)
        q.append(newNode)
        front.left = newNode

        data = int(input("Enter the data : "))
        if data == -1:
            return root
        newNode = Node(data)
        q.append(newNode)
        front.right = newNode


def bfs(root):
    if not root:
        return

    q = [root]

    while len(q) > 0:
        print(q[0].val, end="|")
        front = q.pop(0)

        if front.left is not None:
            q.append(front.left)

        if front.right is not None:
            q.append(front.right)


newRoot = create()
bfs(newRoot)
