from Binarysearchtree import Node
from Binarysearchtree import BinarySearchTree

class Same_tree(BinarySearchTree):
    def is_same(self, bst_b):
        return self.__is_same(self._root, bst_b._root)

    def __is_same(self, bst_a, bst_b):
        if bst_a is None and bst_b is None:
            return True
        if bst_a is not None and bst_b is not None:
            return bst_a._item == bst_b._item and self.__is_same(bst_a._left, bst_b._left) and self.__is_same(bst_a._right, bst_b._right)
        return False

if __name__ == '__main__':
    numbers = [6, 4, 8, 7, 9, 5, 1, 3, 2]
    bst_a = Same_tree()
    bst_b = Same_tree()
    for num in numbers:
        bst_a.add(num)
        bst_b.add(num)

    bst_a.print_inorder()
    print()
    print(bst_a.is_same(bst_b))
    bst_b.add(10)
    print(bst_a.is_same(bst_b))