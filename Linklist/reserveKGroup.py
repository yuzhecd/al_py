from linklist_f import LinkList
from linklist_f import Node

def reverseKGroup(alist, k):
    if alist.head.next is None or k < 2:
        return alist.head.next
    next_head = alist.head.next
    for _ in range(k-1):
        next_head = next_head.next
        if next_head is None:
            return alist.head.next

    head = next_head
    current = alist.head.next
    while next_head:
        tail = current
        pre = None
        for _ in range(k):
            if next_head is not None:
                next_head = next_head.next
            temp = current.next
            current.next = pre
            pre = current
            current = temp
        tail.next = next_head or current
    return head

if __name__ == '__main__':
    ll = LinkList()
    ll.add_last(1)
    ll.add_last(2)
    ll.add_last(3)
    ll.add_last(4)
    ll.add_last(5)
    ll.add_last(6)
    ll.add_last(7)
    ll.add_last(8)
    ll.print_list()
    print()
    result = reverseKGroup(ll, 3)
    l2 = LinkList()
    l2.head.next = result
    l2.print_list()
