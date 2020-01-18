from Binarysearchtree import Node
from Binarysearchtree import BinarySearchTree

def pre_in_build(in_order, pre_order):
    if in_order:
        ind = in_order.index(pre_order.pop(0))
        root = Node(in_order[ind])
        root._left = pre_in_build(in_order[0:ind], pre_order)
        root._right = pre_in_build(in_order[ind + 1:], pre_order)
        return root

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def pre_in_build_common(in_order, pre_order, in_start, in_end, pre_start, pre_end):



if __name__ == '__main__':
    pre_order = [3, 9, 20, 15, 7]
    in_order = [9, 3, 15, 20, 7]

    root = pre_in_build(in_order, pre_order)

    bst = BinarySearchTree()
    bst._root = root
    bst.print_inorder()