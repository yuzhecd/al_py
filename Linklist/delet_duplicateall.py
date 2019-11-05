from linklist_f import LinkList
from linklist_f import Node

def delet_duplicate(alist):
    dummy = pre = alist.head
    head = alist.head.next


    while head is not None and head.next is not None:
        if head.value == head.next.value:
            while head is not None and head.next is not None and head.value == head.next.value:
                head = head.next
            head = head.next
            pre.next = head
        else:
            pre = pre.next
            head = head.next

    return dummy

if __name__ == '__main__':
    ll = LinkList()
    ll.add_last(1)
    ll.add_last(1)
    ll.add_last(1)
    ll.add_last(2)
    ll.add_last(2)
    ll.add_last(3)
    ll.add_last(4)
    ll.add_last(4)
    ll.add_last(5)
    ll.add_last(6)
    ll.add_last(7)
    ll.add_last(7)
    ll.print_list()
    print()
    result = delet_duplicate(ll)
    l2 = LinkList()
    l2.head = result
    l2.print_list()