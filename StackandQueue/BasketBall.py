def score_get(s):
    result = []
    for i in s:
        if i == 'C':
            result.pop()
        elif i == 'D':
            result.append(result[-1]*2)
        elif i == '+':
            result.append(result[-1] + result[-2])
        else:
            result.append(i)
    print(sum(result))

if __name__ == '__main__':
    s = [4, 3, 'C', 'D', '+']
    score_get(s)
