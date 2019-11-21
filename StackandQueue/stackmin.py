from stack_list import Arraystack
class stackwithmin:
    def __init__(self):
        self.stack = Arraystack()
        self.min = Arraystack()

    def push(self, value):
        self.stack.push(value)
        if self.min.is_empty():
            self.min.push(value)
        else:
            self.min.push(min(value, self.min.top()))

    def pop(self):
        if self.stack.is_empty():
            raise ValueError("Stack is empty")
        self.stack.pop()
        self.min.pop()

    def min_stack(self):
        if self.min.is_empty():
            raise ValueError("Stack is empty")
        return self.min.top()

    def print_stack(self):
        self.stack.printstack()
        self.min.printstack()

if __name__ == '__main__':
    mystack = stackwithmin()
    mystack.push(4)
    mystack.push(2)
    mystack.push(3)
    mystack.push(1)
    mystack.push(5)
    mystack.print_stack()
    print(mystack.min_stack())
    mystack.pop()
    mystack.pop()
    mystack.print_stack()
    print(mystack.min_stack())
    mystack.pop()
    mystack.pop()
    mystack.pop()
    mystack.min_stack()
