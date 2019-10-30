from linklist_f import LinkList
from linklist_f import Node 

def merge_list(node_a, node_b):
    dummy = cur = Node()
    while node_a != None and node_b !=None:
        if node_a.value <= node_b.value:
            cur.next = node_a
            node_a = node_a.next
        else:
            cur.next = node_b
            node_b = node_b.next
        cur = cur.next

    cur.next = node_a or node_b
    return dummy.next
    

def merge_list2(list_a, list_b):
    a = list_a.head.next
    b = list_b.head.next
    result = c = Node()
    while a != None and b != None:
        if a.value <= b.value:
            c.next = a
            a = a.next
        else:
            c.next = b
            b = b.next
        c = c.next
    c.next = a or b
    ll = LinkList()
    ll.head.next = result.next
    return ll

def merge_recursive(a, b):
    if not a or  not b:
        return a or b

    if a.value < b.value:
        a.next = merge_recursive(a.next, b)
        return a
    else:
        b.next = merge_recursive(a, b.next)
        return b


if __name__ == '__main__':
    ll_a = LinkList()
    ll_a.add_last(1)
    ll_a.add_last(3)
    ll_a.add_last(5)
    ll_a.add_last(7)
    ll_b = LinkList()
    ll_b.add_last(2)
    ll_b.add_last(4)
    ll_b.add_last(5)
    ll_b.add_last(8)
    ll_b.add_last(10)
    ll_b.add_last(12)

    node1 = Node(1)
    node2 = Node(3)
    ndoe3 = Node(5)
    node1.next = node2
    node2.next = ndoe3

    node_a = Node(2)
    node_b = Node(4)
    node_c = Node(5)
    node_d = Node(8)
    node_a.next = node_b
    node_b.next = node_c
    node_c.next = node_d
    #result = merge_list(node1, node_a)
    
    #ll = LinkList()
    #ll.head.next = result
    #ll.print_list()
    #print()

    result2 = merge_list2(ll_a, ll_b)
    result2.print_list()
    print()

    result3 = merge_recursive(node1, node_a)
    l2 = LinkList()
    l2.head.next = result3
    l2.print_list()