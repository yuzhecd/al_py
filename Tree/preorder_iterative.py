from Binarysearchtree import Node
from Binarysearchtree import BinarySearchTree

class BinarySearchTree_preorder_iterative(BinarySearchTree):
   def preorder_iterative(self):
       return self.__preorder_iterative(self._root)

   def __preorder_iterative(self, node):
       ret = []
       stack = [node]

       while stack:
           node = stack.pop()
           if node:
               ret.append(node._item)
               stack.append(node._right)
               stack.append(node._left)
       print(ret)

if __name__ == '__main__':
    numbers = [8, 4, 3, 7, 5, 6, 12, 10, 15]
    bst = BinarySearchTree_preorder_iterative()
    for nu in numbers:
        bst.add(nu)

    bst.print_preorder()
    print()
    bst.preorder_iterative()