from linklist_f import LinkList
from linklist_f import Node

class LinklistStack(object):
    def __init__(self):
        self._data = LinkList()

    def __len__(self):
        return self._data.size

    def is_empty(self):
        return self._data.size == 0

    def push(self, value):
        return self._data.add_first(value)

    def pop(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
        return self._data.remove_first()

    def top(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
        return self._data.head.next.value

    def printstack(self):
        return self._data.print_list()

if __name__ == '__main__':
    mystack = LinklistStack()
    mystack.push(1)
    mystack.push(2)
    mystack.push(3)
    mystack.push(4)
    mystack.push(5)
    mystack.push(6)
    mystack.printstack()
    print(len(mystack))
    print(mystack.top())
    print(mystack.is_empty())
    mystack.pop()
    mystack.pop()
    mystack.pop()
    mystack.pop()
    mystack.printstack()
    print(len(mystack))
    print(mystack.top())
    mystack.pop()
    mystack.pop()
    print(mystack.is_empty())
    mystack.top()
