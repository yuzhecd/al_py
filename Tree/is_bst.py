from Binarysearchtree import Node
from Binarysearchtree import BinarySearchTree
import sys

class BinarySearchTree_withjudge(BinarySearchTree):
    def is_bst(self):
        return self.__is_bst(self._root, -sys.maxsize, sys.maxsize)

    def __is_bst(self, bst, minmal, maxmal):
        if bst is None:
            return True
        if bst._item <= minmal or bst._item >= maxmal:
            return False
        return self.__is_bst(bst._left, minmal, bst._item) and self.__is_bst(bst._right, bst._item, maxmal)

if __name__ == '__main__':
    numbers = [6, 4, 8, 7, 9, 2, 1, 3, 5, 13, 11, 10, 12] 
    bst = BinarySearchTree_withjudge()   
    for num in numbers:
        bst.add(num)
    bst.print_inorder()
    print()
    print(bst._root._item)
    print(bst.max_depth())
    print(bst.min_depth())
    print(bst.is_bst())