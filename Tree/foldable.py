from Binarysearchtree import Node
from Binarysearchtree import BinarySearchTree

class Foldable_tree(BinarySearchTree):
    def foldable(self):
        return self.__foldable(self._root._left, self._root._right)

    def __foldable(self, node_a, node_b):
        if node_a is None and node_b is None:
            return True
        if node_a is None or node_b is None:
            return False
        return self.__foldable(node_a._left, node_b._right) and self.__foldable(node_a._right, node_b._left)

if __name__ == '__main__':
    numbers_a = [6, 4, 8, 7, 9, 5, 1, 3, 2]
    numbers_b = [6, 5, 7, 4, 8, 3, 9, 2, 10]
    bst_a = Foldable_tree()
    bst_b = Foldable_tree()
    for num in numbers_a:
        bst_a.add(num)
    for num in numbers_b:
        bst_b.add(num)

    bst_a.print_inorder()
    print()
    bst_b.print_inorder()
    print()
    print(bst_a.foldable())
    print(bst_b.foldable())