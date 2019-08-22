from time import time

def ruler_bad(n):
    if n == 1:
        return "1" 
    return ruler_bad(n-1) + ' ' + str(n) + ' ' + ruler_bad(n-1)

def ruler_right(n):
    if n == 1:
        return "1"
    t = ruler_right(n-1)
    return t + ' ' + str(n) + ' ' + t

def ruler_factor(n):
    result = ''
    for i in range(1, n+1):
        result = result  + str(i) + ' ' + result
    return result

if __name__ == '__main__':
    n = int(input('Please input a number: '))
    start = time()
    result_bad = ruler_bad(n)
    end = time()
    print(result_bad)
    print(end - start)

    start = time()
    result_right = ruler_right(n)
    end = time()
    print(result_right)
    print(end - start)

    start = time()
    result_factor = ruler_factor(n)
    end = time()
    print(result_factor)
    print(end - start , result_bad == result_right, result_right == result_factor)