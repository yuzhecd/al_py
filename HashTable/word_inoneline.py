def if_oneline(s):
    line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
    result = []
    for target in s:
        temp = set(target.lower())
        if temp.issubset(line1) or temp.issubset(line2) or temp.issubset(line3):
            result.append(target)
    print(result)

if __name__ == '__main__':
    s = ['Hello', 'Alaska', 'Dad', 'Peace']
    if_oneline(s)