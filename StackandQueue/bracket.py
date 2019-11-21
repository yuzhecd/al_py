def check_bracket(t):
    stack = []
    for c in t:
        if c == '{' or c == '[' or c == '(':
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            if (stack[-1] == '{' and c == '}') or (stack[-1] == '[' and c == ']') or (stack[-1] == '(' and c == ')'):
                stack.pop()
            else:
                return False
    return len(stack) == 0


if __name__ == '__main__':
    t = ['[', '{', '}', '(', ')', ']']
    result = check_bracket(t)
    print(result)