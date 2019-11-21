class Arraystack(object):
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, value):
        self._data.append(value)

    def pop(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
        return self._data.pop()

    def top(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
        return self._data[-1]

    def printstack(self):
        for i in range(len(self._data)-1, -1, -1):
            print(self._data[i], end=' ')
        print()

if __name__ == '__main__':
    mystack = Arraystack()
    mystack.push(1)
    mystack.push(2)
    mystack.push(3)
    mystack.push(4)
    mystack.push(5)
    mystack.push(6)
    em = mystack.is_empty()
    print(em)
    mystack.printstack()
    top = mystack.top()
    print(top)
    print(len(mystack))
    mystack.pop()
    mystack.pop()
    mystack.pop()
    mystack.pop()
    mystack.printstack()
    result = mystack.top()
    print(result)
    mystack.pop()
    mystack.pop()
    e = mystack.is_empty()
    print(e)