def greater_cycle(s):
    stack = []
    result = []
    for c in s:
        if len(stack) == 0 or stack[-1] > c:
            stack.append(c)
        else:
            while len(stack) != 0 and stack[-1] < c:
                temp = stack.pop()
                result.append((temp, c))
            stack.append(c)

    for c in s:
        while len(stack) != 0 and stack[-1] < c:
            temp = stack.pop()
            result.append((temp, c))

    print(result)

if __name__ == '__main__':
    s = [6, 4, 5, 23, 8, 3, 9, 7]
    greater_cycle(s)