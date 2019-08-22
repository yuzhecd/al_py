from time import time
def find_min(b, a):
    start = time()
    c = []
    while b > a:
        if b >= 2*a:
            if b % 2 == 1:
                c.append(1)
                b -= 1
            else:
                c.append(2)
                b = b // 2
        else:
            d = int(b - a)
            for i in range(d):
                c.append(1)
                b -= 1
    e = str(a)
    for i in range(len(c) - 1, -1, -1):
        if c[i] == 2:
            e =  e + ' * 2'
        else:
            e = '(' + e + ' + 1)'
    end = time()
    print(e)
    return end -start

def find_recursion(b, a):
    if b == a:
        return str(a) 
    if b % 2 == 1:
        mid = find_recursion(b-1, a)
        return '(' + mid + ' + 1)'
    if b > 2*a:
        mid = find_recursion(b // 2, a)
        return  mid + ' * 2'
    mid = find_recursion(b-1, a)
    return '(' + mid + ' + 1)' 

if __name__ == '__main__':
    time_f = find_min(10001, 52)
    print('The calculate of "For" time is {}'.format(time_f))
    start = time()
    result_re = find_recursion(10001, 52)
    end = time()
    time_re = end - start
    print(result_re)
    print('The calculate of "Recursion" is {}'.format(time_re))