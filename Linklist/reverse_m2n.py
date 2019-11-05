from linklist_f import LinkList
from linklist_f import Node

def reverse_m2n(alist, m, n):
    pre = alist.head
    for _ in range(m-1):
        pre = pre.next
    cur = pre.next

    result = None
    for _ in range(n-m+1):
        temp = cur.next
        cur.next = result
        result = cur
        cur = temp
    pre.next.next = cur
    pre.next = result

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
    reverse_m2n(ll, 4, 7)
    ll.print_list()

    