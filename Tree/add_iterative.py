from Binarysearchtree import Node
from Binarysearchtree import BinarySearchTree

class BinarySearchTree_withadd_iterative(BinarySearchTree):
    def add_iterative(self, value):
         return self.__add_iterative(value, self._root)

    def __add_iterative(self, value, root):
        new_node = Node(value)
        parent = None
        if self._root is None:
            self._root = new_node
            return
        while True:
            parent = root
            if root._item == value:
                return
                
            elif root._item > value:
                root = root._left
                if root == None:
                    parent._left = new_node
                    return
                
            else:
                root = root._right
                if root == None:
                   parent._right = new_node
                   return
                

if __name__ == '__main__':
    numbers= [6, 4, 8, 7, 9, 2, 1, 3, 5, 13, 11, 10, 12]
    bst = BinarySearchTree_withadd_iterative()
    for nu in numbers:
        bst.add(nu)

    bst.print_inorder()
    print()

    bst_iter = BinarySearchTree_withadd_iterative()
    for nu in numbers:
        bst_iter.add_iterative(nu)

    bst_iter.print_inorder()


