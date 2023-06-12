class Queue:
    def __init__(self):
        self.queue = []
        self.front, self.rear = -1, -1

    def enqueue(self, x):
        self.queue.append(x)
        self.rear += 1
        if len(self.queue) > 1:
            self.front = 0

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty!")
            self.front, self.rear = -1, -1
            return -1
        self.front += 1
        return self.queue.pop(0)

    def get_front(self):
        if len(self.queue) != 0:
            return self.queue[0]
        else:
            return -1

    def get_rear(self):
        n = len(self.queue)
        if n != 0:
            return self.queue[n - 1]
        else:
            return -1

    def display(self):
        print(f"The queue is {self.queue}.")
        f = self.get_front()
        r = self.get_rear()
        print(f"The front element is {f} and the rear element is {r}.")


obj = Queue()
obj.enqueue(7)
obj.enqueue(8)
obj.enqueue(6)
obj.dequeue()
obj.dequeue()
obj.enqueue(2)
obj.display()
