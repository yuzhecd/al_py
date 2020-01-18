from Binarysearchtree import Node
from Binarysearchtree import BinarySearchTree

class BinarySearchTree_withfloor(BinarySearchTree):
    def floor(self, target):
        return self.__floor(self._root, target)

    def __floor(self, root, target):
        if root is None:
            return None
        if root._item == target:
            return root._item
        if target < root._item:
            return self.__floor(root._left, target)
        t = self.__floor(root._right, target)
        if t:
            return t
        return root._item

if __name__ == '__main__':
    numbers = [6, 4, 8, 7, 10, 2, 1, 3, 5, 14, 12, 11, 13] 
    bst = BinarySearchTree_withfloor()   
    for num in numbers:
        bst.add(num)
    bst.print_inorder()
    print()
    print(bst.max_depth())
    print(bst.min_depth())
    print(bst.floor(9))