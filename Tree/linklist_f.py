class Node():
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkList():
    def __init__(self):
        self.head = Node()
        self.size = 0

    def add_first(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def add_last(self, value):
        new_node  = Node(value)
        node = self.head
        while node.next != None:
            node = node.next
        node.next = new_node
        self.size += 1

    def remove_first(self):
        self.head.next = self.head.next.next
        self.size -= 1

    def remove_last(self):
        node = self.head
        while node.next.next != None:
            node = node.next
        node.next = None
        self.size -= 1

    def insert_at(self, value, index):
        new_node = Node(value)
        node = self.head
        for _ in range(index):
            node = node.next
        new_node.next = node.next
        node.next = new_node
        self.size += 1

    def remove_at(self, index):
        node = self.head
        for _ in range(index):
            node = node.next
        node.next = node.next.next
        self.size -= 1

    def length(self):
        print()
        print(self.size)
        print()

    def print_list(self):
        node = self.head
        while node.next != None:
            print(node.next.value, end=" ")
            node = node.next

if __name__ == '__main__':
    ll = LinkList()
    ll.add_first(1)
    ll.add_first(2)
    ll.add_first(3)
    ll.length()
    ll.print_list()
    ll.remove_first()
    ll.length()
    ll.print_list()
    ll.remove_last()
    ll.length()
    ll.add_last(10)
    ll.length()
    ll.print_list()
    ll.add_last(12)
    ll.add_last(14)
    ll.add_last(16)
    ll.print_list()
    ll.length()
    ll.remove_at(1)
    ll.print_list()
    ll.insert_at(100, 1)
    ll.length()
    ll.print_list()