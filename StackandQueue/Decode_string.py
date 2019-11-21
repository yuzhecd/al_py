def decode(s):
    stack = [['', 1]]
    num = ''
    for c in s:
        if c.isdigit():
            num = int(c)
        elif c == '[':
            stack.append(['', num])
        elif c == ']':
            temp_string, k = stack.pop()
            stack[-1][0] += temp_string * k
        else:
            stack[-1][0] += c
    return stack[0][0]

if __name__ == '__main__':
    s = '4[a3[bc2[d]]]'
    p = '4[a]5[d]ef'
    result = decode(p)
    print(result)