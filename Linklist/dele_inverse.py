from linklist_f import LinkList
from linklist_f import Node

def dele_reverse(llist, n):
    fast = llist.head
    slow = llist.head
    while n != 0:
        fast = fast.next
        n -= 1

    while fast != None:
        fast = fast.next
        slow = slow.next
    if slow.next != None:
        slow.value = slow.next.value
        slow.next = slow.next.next
        llist.size -= 1
    else:
        slow.value = None
        slow.next = None
        llist.size -= 1

    return llist

if __name__ == '__main__':
    ll = LinkList()
    ll.add_last(1)
    ll.add_last(2)
    ll.add_last(3)
    ll.add_last(4)
    ll.print_list()
    print()
    ll.length()
    print()
    result = dele_reverse(ll,4)
    result.print_list()
    print()
    ll.length()