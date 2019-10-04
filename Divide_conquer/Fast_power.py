from time import time
def fast_power(a, b):
    sum = 1
    base = a
    while(b != 0):
        if (b & 1) == 1:
            sum *= base
        b = b >> 1
        base *= base
    return sum

if __name__ == '__main__':
    start = time()
    result = fast_power(2, 20)
    end = time() -  start
    print(result, end)