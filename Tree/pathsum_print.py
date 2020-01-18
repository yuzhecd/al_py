from Binarysearchtree import Node
from Binarysearchtree import BinarySearchTree

class BinarySearchTree_withsumpathprint(BinarySearchTree):
    def sumpath_print(self, s):
        if not self._root:
            return []
        ls = []
        re = []
        self.__sumpath_print(self._root, s, ls, re)
        return re

    def __sumpath_print(self, node, s, ls, re):

        if not node._left and not node._right and node._item == s:
            ls.append(node._item)
            re.append(ls)

        if node._left:
            self.__sumpath_print(node._left, s-node._item, ls+[node._item], re)

        if node._right:
            self.__sumpath_print(node._right, s-node._item, ls+[node._item], re)

if __name__ == '__main__':
    numbers = [6, 4, 8, 7, 9, 2, 1, 3, 5, 13, 11 ,10, 12]
    bst = BinarySearchTree_withsumpathprint()
    for nu in numbers:
        bst.add(nu)

    bst.print_inorder()
    print()
    print(bst.sumpath_print(15))

