from Binarysearchtree import Node
from Binarysearchtree import BinarySearchTree

class BinarySearchTree_withpathsumany(BinarySearchTree):
    def pathsum_any(self, target):
        return self.__pathsum_any(self._root, target)

    def pathsum_any_helper(self, node, target):
        if node:
            return int(node._item == target) + \
                self.pathsum_any_helper(node._left, target - node._item) + \
                self.pathsum_any_helper(node._right, target - node._item) 
        return 0
    
    def __pathsum_any(self, node, target):
        if node:
            return self.pathsum_any_helper(node, target) + \
                self.__pathsum_any(node._left, target) + \
                self.__pathsum_any(node._right, target)
        return 0

if __name__ == '__main__':
    numbers = [6, 4, 8, 7, 9, 2, 1, 3, 5, 13, 11 ,10, 12]
    bst = BinarySearchTree_withpathsumany()
    for nu in numbers:
        bst.add(nu)

    bst.print_inorder()
    print()
    print(bst.pathsum_any(4))
    print()
    print(bst.pathsum_any(15))