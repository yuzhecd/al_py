from Binarysearchtree import Node
from Binarysearchtree import BinarySearchTree

class Mirror_tree(BinarySearchTree):
    def mirror(self):
       return self.__mirror(self._root)

    def __mirror(self, node):
        if node is not None:
            self.__mirror(node._left)
            self.__mirror(node._right)

            node._left, node._right = node._right, node._left

if __name__ == '__main__':
    numbers = [6, 4, 8, 7, 9, 5, 1, 3, 2]
    bst = Mirror_tree()
    for num in numbers:
        bst.add(num)

    bst.print_inorder()
    print()
    bst.mirror()
    bst.print_inorder()