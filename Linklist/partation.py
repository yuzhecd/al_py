from linklist_f import LinkList
from linklist_f import Node

def partation(alist, target):
    dummy_left = left_head = Node()
    dummy_right = right_head = Node()
    head = alist.head.next

    while head is not None:
        if target.value > head.value:
            left_head.next = head
            left_head = left_head.next
            head = head.next
        else:
            right_head.next = head
            right_head = right_head.next
            head = head.next
    left_head.next = target
    target.next = dummy_right.next
    right_head.next = None
    return dummy_left

if __name__ == '__main__':
    ll = LinkList()
    ll.add_last(8)
    ll.add_last(3)
    ll.add_last(7)
    ll.add_last(2)
    ll.add_last(1)
    ll.add_last(9)
    t = Node(5)
    result = partation(ll, t)
    l2 = LinkList()
    l2.head = result
    l2.print_list()
