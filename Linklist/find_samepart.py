from linklist_f import LinkList
from linklist_f import Node

# first method, find the difference of length of each list
def find_same(a, b):
    head_a = a
    head_b = b

    length_a, length_b = 0, 0
    while head_a is not None:
        head_a = head_a.next
        length_a += 1

    while head_b is not None:
        head_b = head_b.next
        length_b += 1

    if length_a > length_b:
        diff = length_a - length_b
    else:
        diff = length_b - length_a

    head_a = a
    head_b = b
    while diff != 0:
        if length_a > length_b:
            head_a = head_a.next
            diff -= 1
        else:
            head_b = head_b.next
            diff -= 1

    while head_a != None or head_b != None:
        if head_a == head_b:
            return head_a.value
        else:
            head_a = head_a.next
            head_b = head_b.next

#second method, 

def find_same2(a, b):
    head_a = a
    head_b = b
    while a != b:
        a = a.next if a else head_b
        b = b.next if b else head_a
    return a.value


if __name__ == '__main__':
    a1 = Node(1)
    a2 = Node(3)
    a3 = Node(5)
    c1 = Node(9)
    c2 = Node(10)
    c3 = Node(11)
    b1 = Node(2)
    b2 = Node(4)
    b3 = Node(6)
    b4 = Node(8)

    a1.next = a2
    a2.next = a3
    a3.next = c1
    c1.next = c2
    c2.next = c3
    b1.next = b2
    b2.next = b3
    b3.next = b4
    b4.next = c1

    result = find_same(a1, b1)
    print(result)

    result2 = find_same2(a1, b1)
    print(result2)