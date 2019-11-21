from stack_list import Arraystack

#O(n^2)
def sort_stack(target):
    result = Arraystack()
    while target:
        temp = target.pop()
        while not result.is_empty() and result.top() < temp:
            target.push(result.pop())
        result.push(temp)

    return result

if __name__ == '__main__':
    my_stack = Arraystack()
    my_stack.push(3)
    my_stack.push(7)
    my_stack.push(1)
    my_stack.push(4)
    my_stack.push(6)
    my_stack.push(9)
    my_stack.printstack()
    result = sort_stack(my_stack)
    result.printstack()


