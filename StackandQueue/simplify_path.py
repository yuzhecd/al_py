def simplify(s):
    a = s.split('/')
    result = []
    for i in a:
        if i == '.':
            continue
        elif i == '':
            continue
        elif i == '..' and len(result) != 0:
            result.pop()
        else:
            result.append(i)
    return '/' + '/'.join(result)

if __name__ == '__main__':
    s = '/c/b/a/e/../.././f'
    result = simplify(s)
    print(result)
