class two_stack:
    def __init__(self):
        DEFAULTCAPACITY = 10
        self._size_first = 0
        self._size_second = 0
        self._size = 0
        self._data = [None] * DEFAULTCAPACITY

    def push_first(self, value):
        if self._size >= len(self._data):
            raise ValueError('stack overflow')
        self._data[self._size_first] = value
        self._size_first += 1
        self._size += 1

    def push_second(self, value):
        if self._size >= len(self._data):
            raise ValueError('stack overflow')
        self._data[-self._size_second-1] = value
        self._size_second += 1
        self._size += 1

    def pop_first(self):
        if self._size_first <= 0:
            raise ValueError("first stack is underflow")
        temp = self._data[self._size_first-1]
        self._data[self._size_first-1] = None
        self._size_first -= 1
        self._size -= 1
        return temp

    def pop_second(self):
        if self._size_second <= 0:
            raise ValueError("second stack is underflow")
        temp = self._data[-self._size_second]
        self._data[-self._size_second] = None
        self._size_second -= 1
        self._size -= 1
        return temp

if __name__ == '__main__':
    my_stack = two_stack()
    my_stack.push_first(1)
    my_stack.push_first(2)
    my_stack.push_first(3)
    my_stack.push_first(4)
    my_stack.push_first(5)
    my_stack.push_second(10)
    my_stack.push_second(9)
    my_stack.push_second(8)
    my_stack.push_second(7)
    print(my_stack._data)
    my_stack.pop_first()
    print(my_stack._data)
    my_stack.pop_second()
    print(my_stack._data)
    my_stack.push_second(11)
    my_stack.push_second(12)
    my_stack.push_second(13)
    print(my_stack._data)
    my_stack.pop_first()
    my_stack.pop_first()
    my_stack.pop_first()
    my_stack.pop_first()
    print(my_stack._data)
