from Binarysearchtree import Node
from Binarysearchtree import BinarySearchTree

def is_balanced(bst):
    return bst.max_depth() - bst.min_depth() <= 1


if __name__ == '__main__':
    numbers = [6, 4, 8, 7, 9, 2, 1, 3, 5, 13, 11, 10, 12] 
    bst = BinarySearchTree()   
    for num in numbers:
        bst.add(num)
    bst.print_inorder()
    print()
    print(bst.max_depth())
    print(bst.min_depth())
    print(is_balanced(bst))