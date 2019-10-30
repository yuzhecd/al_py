from linklist_f import LinkList

def find_mid(llist):
    assert llist.head is not None and llist.head.next is not None
    fast = llist.head
    slow = llist.head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    return slow.value


if __name__ == '__main__':
    ll = LinkList()
    ll.add_first(1)
    ll.add_last(2)
    ll.add_last(3)
    ll.print_list()
    if ll.head is not None:
        print('right')

    result = find_mid(ll)
    print(result)