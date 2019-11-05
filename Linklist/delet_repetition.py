from linklist_f import LinkList
from linklist_f import Node

def delet_repe(alist):
    dummy = alist.head
    cur = alist.head.next

    while cur.next is not None:
        if cur.value == cur.next.value:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy

if __name__ == '__main__':
    ll = LinkList()
    ll.add_last(1)
    ll.add_last(1)
    ll.add_last(1)
    ll.add_last(2)
    ll.add_last(2)
    ll.add_last(2)
    ll.add_last(2)
    ll.add_last(2)
    ll.add_last(2)
    ll.add_last(3)
    ll.add_last(4)
    ll.add_last(4)
    ll.add_last(4)
    ll.print_list()
    print()
    result = delet_repe(ll)
    ll.print_list()