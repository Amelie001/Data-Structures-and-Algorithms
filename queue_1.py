
class Queue: 

    def __init__(self, size): 
        self.queue = [None] * size
        self.front = 0 
        self.rear = 0 
        self.size = size 
        self.available = size 

    def enqueue(self, item): 
        if self.available == 0: 
            print("Queue overflow!")

        else: 
            self.queue[self.rear] = item 
            self.rear = (self.rear + 1) % self.size 
            self.available -= 1

    def dequeue(self): 
        if self.available == self.size: 
            print("Queue underflow!")

        else: 
            self.queue[self.front] = None
            self.queue=(self.front + 1) % self.size
            self.available += 1

    def peek(self): 
        print(self.queue[self.front])

    def getRear(self): 
        print(self.queue[self.rear])

    def print_queue(self): 
        print(self.queue)

queue1 = Queue(4)
queue1.enqueue(10)
queue1.peek()
queue1.getRear()
queue1.enqueue(20)
queue1.dequeue()
queue1.peek()
queue1.print_queue()
