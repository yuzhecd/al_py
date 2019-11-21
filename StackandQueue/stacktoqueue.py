class Stackedqueue:
    def __init__(self):
        self.pushstack = []
        self.popstack = []

    def enqueue(self, value):
        self.pushstack.append(value)

    def dequeue(self):
        if not self.pushstack and not self.popstack:
            raise ValueError("Queue is empty")
        if not self.popstack:
            while self.pushstack:
                self.popstack.append(self.pushstack.pop())
        answer = self.popstack.pop()
        return answer

    def print_queue(self):
        print(self.popstack, end=' ')
        print(self.pushstack, end=' ')
        print()

if __name__ == '__main__':
    myqueue = Stackedqueue()
    myqueue.enqueue(1)
    myqueue.enqueue(2)
    myqueue.enqueue(3)
    myqueue.enqueue(4)
    myqueue.enqueue(5)
    myqueue.print_queue()
    result = myqueue.dequeue()
    print(result)
    myqueue.print_queue()
    result2 = myqueue.dequeue()
    print(result2)
    myqueue.print_queue()
    myqueue.enqueue(6)
    myqueue.enqueue(7)
    myqueue.print_queue()
    myqueue.dequeue()
    myqueue.print_queue()
    myqueue.dequeue()
    myqueue.dequeue()
    myqueue.dequeue()
    myqueue.dequeue()
    myqueue.print_queue()