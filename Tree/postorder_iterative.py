from Binarysearchtree import Node 
from Binarysearchtree import BinarySearchTree

class BinarySearchTree_postorder_iterative(BinarySearchTree):
    def postorder_iterative(self):
        return self.__postorder_iterative(self._root)

    def __postorder_iterative(self, node):
        stack = []
        stack.append((node, False))

        while stack:
            node, visit = stack.pop()
            if node:
                if visit:
                    print(node._item, end=' ')
                else:
                    stack.append((node, True))
                    stack.append((node._right, False))
                    stack.append((node._left, False))

if __name__ == '__main__':
    numbers = [8, 4, 3, 7, 5, 6, 12, 10, 15]
    bst = BinarySearchTree_postorder_iterative()
    for nu in numbers:
        bst.add(nu)

    bst.print_postorder()
    print()
    bst.postorder_iterative()
