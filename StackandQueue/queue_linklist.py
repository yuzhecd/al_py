from linklist_f import LinkList
from linklist_f import Node

class LinkedQueue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._count = 0

    def __len__(self):
        return self._count

    def is_empty(self):
        return self._count == 0

    def first(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self._head.value

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        answer = self._head.value
        self._head = self._head.next
        self._count -= 1
        return answer


    def equeue(self, value):
        new = Node(value)
        if self._head is None:
            self._head = new
            self._tail = new
        else:
            self._tail.next = new
            self._tail = self._tail.next
        self._count += 1

    def printqueue(self):
        head = self._head
        while head is not None:
            print(head.value, end=' ')
            head = head.next
        print()

if __name__ == '__main__':
    myqueue = LinkedQueue()
    myqueue.equeue(1)
    myqueue.equeue(2)
    myqueue.equeue(3)
    myqueue.equeue(4)
    myqueue.equeue(5)
    myqueue.equeue(6)
    myqueue.printqueue()
    print(myqueue._count)
    print(myqueue.dequeue())
    myqueue.dequeue()
    myqueue.dequeue()
    myqueue.dequeue()
    myqueue.dequeue()
    myqueue.dequeue()
    print(len(myqueue))
    print(myqueue.is_empty())
    myqueue.equeue(10)
    print(myqueue._head.value)
    print(len(myqueue))