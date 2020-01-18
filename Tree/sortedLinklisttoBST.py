from linklist_f import Node
from linklist_f import LinkList
from Binarysearchtree import Node as Nd
from Binarysearchtree import BinarySearchTree

def LinkListtoBST(head):
    if head is None:
        return None

    dummy = Node(0)
    dummy.next = head

    fast = dummy
    slow = dummy
    slow_tail = dummy

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow_tail = slow
        slow = slow.next

    slow_tail.next = None
    node = Nd(slow.value)
    node._left = LinkListtoBST(dummy.next)
    node._right = LinkListtoBST(slow.next)
    return node

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    

    bst = BinarySearchTree()
    result = LinkListtoBST(node1)
    bst._root = result
    bst.print_inorder()