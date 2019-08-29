import unittest
def binary_for(alist, item):
    left, right = 0, len(alist) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if alist[mid] == item:
            return mid
        elif alist[mid] > item:
            right = mid - 1 
        else:
            left = mid + 1
    return -1

class test_binary(unittest.TestCase):
    def setUp(self):
        self._f = binary_for

    def test_empty(self):
        alist = []
        r = self._f(alist, 5)
        self.assertEqual(r, -1)

    def test_one(self):
        alist = [1]
        r = self._f(alist, 1)
        self.assertEqual(r, 0)
        r = self._f(alist, 0)
        self.assertEqual(r, -1)

    def test_two(self):
        alist = [1, 10]
        r = self._f(alist, 1)
        self.assertEqual(r, 0)
        r = self._f(alist, 0)
        self.assertEqual(r, -1)
        r = self._f(alist, 10)
        self.assertEqual(r, 1)
    
if __name__ == '__main__':
    a = test_binary()
    a.setUp()
    a.test_empty()
    a.test_one()
    a.test_two()