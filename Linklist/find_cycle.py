from linklist_f import LinkList
from linklist_f import Node

def find_cycle(llist):
    return find_cycle_helper(llist.head)

def find_cycle_helper(head):
    if head is None:
        return False

    fast = head
    slow = head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.next = node2
    node2.next = node3
    node3.next = node1

    result = find_cycle_helper(node1)
    print(result)