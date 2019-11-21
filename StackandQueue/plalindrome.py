def plalin_stack(p):
    temp = p.copy()
    result = []
    while temp:
        result.append(temp.pop())
    return result == p


if __name__ == '__main__':
    p = [1, 2, 3, 4, 3, 2, 1]
    print(plalin_stack(p))