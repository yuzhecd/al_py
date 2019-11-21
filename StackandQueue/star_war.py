def star_war(s):
    stack = []
    for c in s:
        if c >= 0:
            stack.append(c)
        elif len(stack) == 0 or stack[-1] < 0:
            stack.append(c)
        elif abs(stack[-1]) > abs(c): 
            continue
        else:
            while (len(stack) != 0) and (abs(stack[-1]) <= abs(c)):
                stack.pop()
            if len(stack) == 0:
                stack.append(c)
    print(stack)

if __name__ == '__main__':
    s = [-2, -1, 1, 2]
    p = [10 ,2, -5]
    m = [5, 10, -5]
    star_war(s)