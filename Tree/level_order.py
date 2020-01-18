#按层打印
from Binarysearchtree import Node
from Binarysearchtree import BinarySearchTree

class BinarySearchTree_with_levelorder(BinarySearchTree):
    def level_order(self):
        return self.__level_order(self._root)
    
    def __level_order(self, root):
        if not root:
            print('None')
        
        level = [root]
        ret = []
        while level:
            #CurrentNodes = []
            Nextlevel = []
            for node in level:
                if node:
                    ret.append(node._item)
                    #CurrentNodes.append(node._item)
                    #Nextlevel.append(node._left)
                    #Nextlevel.append(node._right)
                    Nextlevel.extend([node._left, node._right])
                    Nextlevel.copy()
            #ret += CurrentNodes
            level = Nextlevel
        print(ret)

    def level_order_reverse(self):
        return self.__level_order_reverse(self._root)

    def __level_order_reverse(self, root):
        ret = []
        level = [root]

        while level:
            #CurrentNodes = []
            Nextlevel = []
            for node in level:
                if node:
                    ret.insert(0, node._item)
                    #CurrentNodes.append(node._item)
                    Nextlevel.append(node._left)
                    Nextlevel.append(node._right)
            #ret += CurrentNodes
            level = Nextlevel
        #ret.reverse()
        print(ret)

    def level_order_zigzag(self):
        return self.__level_order_zigzag(self._root)

    def __level_order_zigzag(self, root):
        ret = []
        level = [root]
        flag = 1

        while level:
            CurrentNodes = []
            Nextlevel = []
            for node in level:
                if node:
                    CurrentNodes.append(node._item)
                    Nextlevel.extend([node._left, node._right])
            ret += CurrentNodes[::flag]
            level = Nextlevel
            flag *= -1
        print(ret)

if __name__ == '__main__':
    numbers = [8, 4, 3, 7, 5, 6, 12, 10, 15]
    bst = BinarySearchTree_with_levelorder()
    for nu in numbers:
        bst.add(nu)

    bst.print_preorder()
    print()
    bst.level_order()
    print()
    bst.level_order_reverse()
    print()
    bst.level_order_zigzag()