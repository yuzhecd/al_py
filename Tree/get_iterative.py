from Binarysearchtree import Node
from Binarysearchtree import BinarySearchTree
from time import time

class BinarySearchTree_withiterativeget(BinarySearchTree):
    def get_iterative(self, value):
        return self.__get_iterative(value, self._root)
    
    def __get_iterative(self, value, root):
        while True:
            if root == None:
                return "Not Found"
            elif root._item == value:
                return value
            elif root._item > value:
                root = root._left
            else:
                root = root._right

if __name__ == '__main__':
    numbers = [6, 4, 8, 7, 9, 2, 1, 3, 5, 13, 11, 10, 12] 
    bst = BinarySearchTree_withiterativeget() 
    for num in numbers:
        bst.add(num)
    bst.print_inorder()
    print()
    start = time()
    print(bst.get(5))
    print()
    print(time() - start)
    print()
    start_2 = time()
    print(bst.get_iterative(5))
    print()
    print(time() - start_2)
    print(bst._root._item)