from stack_list import Arraystack
import sys

class stackwithminsuper(Arraystack):
    def __init__(self):
        super(stackwithminsuper, self).__init__()

    def push(self, value):
        newMin = min(value, self._min())
        super().push(stackwm(value, newMin))

    def _min(self):
        if super().is_empty():
            return sys.maxsize
        else:
            return super().top()._min

    def printstack(self):
        for i in range(len(self._data)-1, -1, -1):
            print(self._data[i]._value, end=' ')
        print()
        for i in range(len(self._data)-1, -1, -1):
            print(self._data[i]._min, end=' ')
        print()


class stackwm:
    def __init__(self, value, minvalue):
        self._value = value
        self._min = minvalue

if __name__ == '__main__':
    mystack = stackwithminsuper()
    mystack.push(4)
    mystack.push(2)
    mystack.push(3)
    mystack.push(7)
    mystack.push(1)
    mystack.printstack()
    print(mystack._min())
    mystack.pop()
    mystack.printstack()
    print(mystack._min())