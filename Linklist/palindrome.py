from linklist_f import LinkList
from linklist_f import Node

def palindrome(alist):
    head = alist.head
    if head == None:
        return head

    #1.find mid point
    fast = head.next
    slow = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    #2.split into two linklist
    head2 = Node()
    if fast == None:
        head2.next = slow.next
        slow.next = None
    else:
        head2.next = slow.next.next
        slow.next = None

    #3.reverse second linklist
    pre = None
    cur = head2.next
    while cur:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp

    # judging if it is palindrome
    while pre.next is not None:
        if pre.value != head.next.value:
            return False
        else:
            pre = pre.next
            head = head.next

    return True

if __name__ == '__main__':
    ll = LinkList()
    ll.add_last(1)
    ll.add_last(2)
    ll.add_last(3)
    ll.add_last(4)
    ll.add_last(3)
    ll.add_last(2)
    ll.add_last(1)
    ll.print_list()
    print()
    result = palindrome(ll)
    print(result)
