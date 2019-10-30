from linklist_f import LinkList

def del_node(node):
    node.value = node.next.value
    node.next = node.next.next

if __name__ == '__main__':
    ll = LinkList()
    ll.add_last(1)
    ll.add_last(2)
    ll.add_last(3)
    ll.print_list()
    del_node(ll.head.next)
    ll.print_list()
    ll.add_first(5)
    ll.print_list()
