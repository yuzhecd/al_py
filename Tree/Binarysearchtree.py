class Node:
    def __init__(self, item=None, left=None, right=None):
        self._item = item
        self._left = left
        self._right = right

class BinarySearchTree:
    def __init__(self, root=None):
        self._root = root
    
    def get(self, value):
        return self.__get(value, self._root)

    def __get(self, value, root):
        if root == None:
            return "not found"
        if root._item == value:
            return value
        elif root._item > value:
            return self.__get(value, root._left)
        else:
            return self.__get(value, root._right)

    # def add(self, value):
    #     self._root = self.__add(self._root, value)
        
    # def __add(self, node, value): # return node ,helper
    #     if (node is None):
    #         return Node(value)
    #     if (value == node._item):
    #         pass
    #     else:
    #         if (value < node._item):
    #             node._left = self.__add(node._left, value)
    #         else:
    #             node._right = self.__add(node._right, value)
    #     return node 

    def add(self, value):
        self._root = self.__add(value, self._root)

    def __add(self, value, node):
        if node is None:
            return Node(value)
        elif node._item > value:
            node._left = self.__add(value, node._left)
        else:
            node._right = self.__add(value, node._right)
        return node

    def remove(self, value):
        return self.__remove(value, self._root)

    def __remove(self, value, root):
        if root == None:
            return None
        if root._item > value:
            root._left = self.__remove(value, root._left)
        if root._item < value:
            root._right = self.__remove(value, root._right)
        else:
            if root._left == None:
                root = root._right
            elif root._right == None:
                root = root._left
            else:
                root._item = self.__get_max(root._left)
                root._left = self.__remove(root._item, root._left)
        return root

    def get_max(self):
        return self.__get_max(self._root)

    def __get_max(self, root):
        node = root
        if node is None:
            return None
        while node._right != None:
            node = node._right
        return node._item

    def print_inorder(self):
        return self.__print_inorder(self._root)

    def __print_inorder(self, root):
        if root is None:
            return None
        self.__print_inorder(root._left)
        print(root._item, end=' ')
        self.__print_inorder(root._right)

    def print_preorder(self):
        return self.__print_preorder(self._root)

    def __print_preorder(self, root):
        if root is None:
            return None
        print(root._item, end=' ')
        self.__print_preorder(root._left)
        self.__print_preorder(root._right)

    def print_postorder(self):
        return self.__print_postorder(self._root)

    def __print_postorder(self, root):
        if root is None:
            return None
        self.__print_postorder(root._left)
        self.__print_postorder(root._right)
        print(root._item, end=' ')

    def size(self):
        return self.__size(self._root)

    def __size(self, root):
        if root is None:
            return 0
        left = self.__size(root._left)
        right = self.__size(root._right)
        return 1 + left + right

    def max_depth(self):
        return self.__max_depth(self._root)

    def __max_depth(self, root):
        if root is None:
            return 0
        max_leftandright = max(self.__max_depth(root._left), self.__max_depth(root._right))
        return 1 + max_leftandright
    
    def min_depth(self):
        return self.__min_depth(self._root)
    
    def __min_depth(self, root):
        if root is None:
            return 0
        min_leftandright = min(self.__min_depth(root._left), self.__min_depth(root._right))
        return 1 + min_leftandright

if __name__ == '__main__':
    numbers = [6, 4, 8, 7, 9, 2, 1, 3, 5, 13, 11, 10, 12] 
    bst = BinarySearchTree()   
    for num in numbers:
        bst.add(num)
    # bst.remove(5)
    bst.print_preorder()
    print()
    bst.print_postorder()
    print()
    bst.print_inorder()
    print()
    print(bst.size())
    print(bst.max_depth())
    print(bst.min_depth())
    # print()
    # bst.add(6)
    # bst.print_preorder()
    # print(bst.get(10))