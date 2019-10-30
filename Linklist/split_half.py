from linklist_f import LinkList
from linklist_f import Node

def half_split(llist):
    assert llist.head is not None and llist.head.next is not None
    fast = llist.head
    slow = llist.head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    new_list = LinkList()
    new_list.head.next = slow.next
    new_list.size = llist.size // 2
    slow.next = None
    llist.size -= llist.size // 2

    return llist, new_list

if __name__ == '__main__':
    ll = LinkList()
    ll.add_last(1)
    ll.add_last(2)
    ll.add_last(3)
    #ll.add_last(4)
    ll.print_list()
    ll.length()
    print()
    front, back = half_split(ll)
    front.print_list()
    front.length()
    print()
    back.print_list()
    back.length()

