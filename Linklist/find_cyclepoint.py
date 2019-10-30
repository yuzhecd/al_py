from linklist_f import LinkList
from linklist_f import Node

def find_cyclepoint(llist):
    return find_cyclepoint_helper(llist.head)

def find_cyclepoint_helper(head):
    assert head is not None and head.next is not None
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            break
    slow = head
    while slow is not None and slow != fast:
        slow = slow.next
        fast = fast.next
        if slow == fast:
            return slow.value

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node4

    result = find_cyclepoint_helper(node1)
    print(result)