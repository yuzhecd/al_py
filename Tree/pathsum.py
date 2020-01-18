from Binarysearchtree import BinarySearchTree
from Binarysearchtree import Node

class BinarySearchTree_withsumpath(BinarySearchTree):
    def sumpath(self, s):
        return self.__sumpath(self._root, s)

    def __sumpath(self, node, s):
        if not node:
            return False

        if not node._right and not node._left and node._item == s:
            return True

        s -= node._item

        return self.__sumpath(node._right, s) or self.__sumpath(node._left, s)

if __name__ == '__main__':
    numbers = [6, 4, 8, 7, 9, 2, 1, 3, 5, 13, 11 ,10, 12]
    bst = BinarySearchTree_withsumpath()
    for nu in numbers:
        bst.add(nu)

    bst.print_inorder()
    print()
    print(bst.sumpath(4))
    print()
    print(bst.sumpath(15))
