from Binarysearchtree import Node
from Binarysearchtree import BinarySearchTree

class BinarySearchTree_withcommonancestor(BinarySearchTree):
    def commonancestor(self, p, q):
        return self.__commonancestor(self._root, p, q)

    def __commonancestor(self, node, p, q):
        while node:
            if node._item > p and node._item > q:
                node = node._left
            elif node._item < p and node._item < q:
                node = node._right
            else:
                return node._item

if __name__ == '__main__':
    numbers = [6, 4, 8, 7, 9, 2, 1, 3, 5, 13, 11 ,10, 12]
    bst = BinarySearchTree_withcommonancestor()
    for nu in numbers:
        bst.add(nu)

    bst.print_inorder()
    print()
    print(bst.commonancestor(4, 8))
    print(bst.commonancestor(10, 13))
    print(bst.commonancestor(1, 7))
