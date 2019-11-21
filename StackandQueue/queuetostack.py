from queue_list import ArrayQueue
class QueuedStack:
    def __init__(self):
        self.stack = ArrayQueue()

    def push(self, value):
        self.stack.enqueue(value)
    
    def pop(self):
        if self.stack._size == 0:
            raise ValueError("Stack is empty")
        for _ in range(1, self.stack._size):
            self.stack.enqueue(self.stack.dequeue())
        return self.stack.dequeue()

    def print_stack(self):
        self.stack.printqueue()

if __name__ == '__main__':
    mystack = QueuedStack()
    mystack.push(1)
    mystack.push(2)
    mystack.push(3)
    mystack.push(4)
    mystack.push(5)
    mystack.push(6)
    mystack.print_stack()
    print(mystack.pop())
    mystack.print_stack()
    print(mystack.pop())
    print(mystack.pop())
    print(mystack.pop())
    print(mystack.pop())
    mystack.print_stack()
    print(mystack.pop())
    mystack.push(10)
    mystack.print_stack()