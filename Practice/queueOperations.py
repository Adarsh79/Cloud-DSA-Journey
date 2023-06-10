class Queue:
    def __init__(self):
        self.queue = []
        self.front, self.rear = -1, -1

    def enqueue(self, x):
        if len(self.queue) == 1:
            self.front = 1
        self.queue.append(x)
        self.rear += 1

    def dequeue(self):
        if len(self.queue) < 1:
            return "No elements in queue to remove!"
        self.front += 1
        return self.queue.pop(0)

    def display(self):
        print(self.queue)


obj = Queue()
