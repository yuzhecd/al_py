class ArrayQueue:
    def __init__(self):
        DEFAULTCAPACITY = 5
        self._data = [None] * DEFAULTCAPACITY 
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, value):
        if self._size == len(self._data):
            self.resize(len(self._data) * 2)
        pos = (self._front + self._size) % len(self._data)
        self._data[pos] = value
        self._size += 1

    def resize(self, mag):
        old = self._data
        self._data = [None] * mag
        for i in range(len(old)):
            pos = (self._front + i) % len(old)
            self._data[i] = old[pos]
        self._front = 0

    def printqueue(self):
        for i in range(self._size):
            pos = (self._front + i) % len(self._data)
            print(self._data[pos], end=' ')
        print()

if __name__ == '__main__':
    myqueue = ArrayQueue()
    myqueue.enqueue(1)
    myqueue.enqueue(2)
    myqueue.enqueue(3)
    myqueue.enqueue(4)
    myqueue.enqueue(5)
    myqueue.dequeue()
    myqueue.dequeue()
    myqueue.enqueue(6)
    #myqueue.enqueue(7)
    #myqueue.enqueue(8)
    print(myqueue._data)
    myqueue.printqueue()
    print(len(myqueue))
    print(myqueue.first())
    print(myqueue.is_empty())
    myqueue.dequeue()
    myqueue.dequeue()
    myqueue.printqueue()
    myqueue.dequeue()
    myqueue.dequeue()
    myqueue.printqueue()
    print(myqueue.is_empty())
    #myqueue.dequeue()
    myqueue.first()
