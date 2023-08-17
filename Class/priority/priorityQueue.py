class PriorityQueue:

    def __init__(self):
        self.nodes = []

    def size(self):
        return len(self.nodes)

    def parent(self, i):
        return (i - 1) // 2

    def swap(self, i, j):
        self.nodes[i], self.nodes[j] = self.nodes[j], self.nodes[i]

    def insert(self, key):
        child = self.size()
        self.nodes.append(key)

        while child != 0:
            p = self.parent(child)
            if self.nodes[p] < self.nodes[child]:
                self.swap(p, child)
            child = p

    def print(self):
        print(self.nodes)


obj = PriorityQueue()
obj.insert(1)
obj.insert(5)
obj.insert(2)
obj.insert(10)
obj.print()
