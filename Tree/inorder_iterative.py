from Binarysearchtree import Node
from Binarysearchtree import BinarySearchTree

class BinarySearchTree_inorder_iterative(BinarySearchTree):
    def inorder_iterative(self):
        return self.__inorder_iterative(self._root)

    def __inorder_iterative(self, node):
        stack = []

        while True:
            while node is not None:
                stack.append(node)
                node = node._left

            if len(stack) == 0:
                return

            node = stack.pop()
            print(node._item, end=' ')
            node = node._right

if __name__ == '__main__':
    numbers= [6, 4, 8, 7, 9, 2, 1, 3, 5, 13, 11, 10, 12]
    bst = BinarySearchTree_inorder_iterative()
    for nu in numbers:
        bst.add(nu)

    bst.print_inorder()
    print()
    bst.inorder_iterative()