def string_reverse(s):
    result = []
    temp = []
    for i in s:
        temp.append(i)
    for _ in s:
        result.append(temp.pop())
    return ''.join(result)


if __name__ == '__main__':
    s = "Hello world"
    r = string_reverse(s)
    print(r)