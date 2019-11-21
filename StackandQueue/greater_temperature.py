def greater_T(s):
    stack = []
    result = []
    for i, c in enumerate(s):
        if len(stack) == 0 or stack[-1][1] > c:
            stack.append([i, c])
        else:
            while len(stack) != 0 and stack[-1][1] < c:
                temp = stack.pop()
                result.append((temp[1], i - temp[0]))
            stack.append([i, c])

    if len(stack) != 0:
        for e in stack:
            result.append((e[1], -1))

    print(result)

if __name__ == '__main__':
    s = [73, 74, 75, 71, 69, 72, 76, 73]
    greater_T(s)