from linklist_f import LinkList
from linklist_f import Node

def reverse_l(alist):
    pre = None
    cur = alist.head.next

    while cur is not None:
        temp = cur.next
        cur.next = pre 
        pre = cur
        cur = temp
    alist.head.next = pre

def reverse_recursion(node):
    if node.next is None:
        return node
    head = reverse_recursion(node.next)
    node.next.next = node
    node.next = None
    return head

if __name__ == '__main__':
    ll = LinkList()
    ll.add_last(1)
    ll.add_last(2)
    ll.add_last(3)
    ll.add_last(4)
    ll.print_list()
    print()
    reverse_l(ll)
    ll.print_list()
    print()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    result = reverse_recursion(node1)
    l2 = LinkList()
    l2.head.next = result
    l2.print_list()
