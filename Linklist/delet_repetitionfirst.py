from linklist_f import LinkList
from linklist_f import Node

def delet_repeall(alist):
    head = alist.head.next

    while head.next is not None:
        if head.value == head.next.value:
            head = head.next
        elif head.next.value == head.next.next.value:
            head = head.next
        else:
            head = head.next
            break

    return head

if __name__ == '__main__':
    ll = LinkList()
    ll.add_last(1)
    ll.add_last(1)
    ll.add_last(1)
    ll.add_last(2)
    ll.add_last(2)
    ll.add_last(2)
    ll.add_last(2)
    ll.add_last(3)
    ll.add_last(4)
    ll.add_last(5)
    ll.add_last(5)
    ll.add_last(5)
    ll.add_last(5)
    ll.print_list()
    print()
    result = delet_repeall(ll)
    l2 = LinkList()
    l2.head.next = result
    l2.print_list()