from linklist_f import LinkList
from linklist_f import Node

def merge(alist):
    dummy = Node(0)
    cur = alist.head.next

    while cur is not None:
        pre = dummy
        while pre.next is not None and pre.next.value < cur.value:
            pre = pre.next
        temp = cur.next
        cur.next = pre.next
        pre.next = cur
        cur = temp
    return dummy.next

if __name__ == '__main__':
    ll = LinkList()
    ll.add_last(9)
    ll.add_last(2)
    ll.add_last(7)
    ll.add_last(8)
    ll.add_last(5)
    ll.add_last(1)
    ll.print_list()
    result = merge(ll)
    print()
    l2 = LinkList()
    l2.head.next = result
    l2.print_list()