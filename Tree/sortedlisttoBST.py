from Binarysearchtree import Node
from Binarysearchtree import BinarySearchTree

class BinarySearchTree_with_insert(BinarySearchTree):
    def insert_balance(self, list_a):
        if not list_a:
            return 
        mid = len(list_a) // 2
        root = Node(list_a[mid])
        root._left = self.insert_balance(list_a[:mid])
        root._right = self.insert_balance(list_a[mid+1:])
        return root

if __name__ == '__main__':
    numbers = [-10, -3, 0, 5, 9]
    bst = BinarySearchTree_with_insert()
    result = bst.insert_balance(numbers)
    bst._root = result
    bst.print_inorder()