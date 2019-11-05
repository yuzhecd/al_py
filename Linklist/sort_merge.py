from linklist_f import LinkList
from linklist_f import Node

def sort_merge(alist):
    return sort_merge_helper(alist.head.next)

def sort_merge_helper(head):
    if head is None or head.next is None:
        return head
    mid = get_mid(head)
    rhead = mid.next
    mid.next = None
    return merge(sort_merge_helper(head),sort_merge_helper(rhead))

def get_mid(node):
    if node is not None:
        return node
    fast = node
    slow = node
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    return slow

def merge(left, right):
    dummy = head = Node(0)
    while left and right:
        if left.value < right.value:
            head.next = left
            left = left.next
        else:
            head.next = right
            right = right.next
        head = head.next
    if left != None:
        head.next = left
    if right != None:
        head.next =right
    return dummy.next

if __name__ == '__main__':
    ll = LinkList()
    ll.add_last(8)
    ll.add_last(3)
    ll.add_last(7)
    ll.add_last(2)
    ll.add_last(1)
    ll.add_last(12)
    ll.add_last(9)

    result = sort_merge(ll)
    l2 = LinkList()
    l2.head.next = result
    l2.print_list()
