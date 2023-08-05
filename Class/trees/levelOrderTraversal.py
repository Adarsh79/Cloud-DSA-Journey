# Level order traversal using linked list
from queue import Queue


class TNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class LNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def traversal(root):
    ans = []

    if root is None:
        return

    ll_node = LNode(root.data)
    ans.append(ll_node)

    pendingNode = Queue()
    pendingNode.put(root)

    while pendingNode.qsize() > 0:
        length = pendingNode.qsize()
        temp_head = temp_tail = None
        for _ in range(length):
            front = pendingNode.get()
            if front.left is not None:
                if temp_head is None:
                    temp_head = LNode(front.left.data)
                    temp_tail = temp_head
                else:
                    newNode = LNode(front.left.data)
                    temp_tail.next = newNode
                    temp_tail = temp_tail.next
                pendingNode.put(front.left)

            if front.right is not None:
                if temp_head is None:
                    temp_head = LNode(front.right.data)
                    temp_tail = temp_head
                else:
                    newNode = LNode(front.right.data)
                    temp_tail.next = newNode
                    temp_tail = temp_tail.next
                pendingNode.put(front.left)

        if temp_head is None:
            continue

        ans.append(temp_head)

    return ans


rootNode = TNode(5)
rootNode.left = TNode(6)
rootNode.right = TNode(7)
print(traversal(rootNode))
