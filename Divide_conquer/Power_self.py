from time import time
def power_self(a, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power_self(a, 1 / n)
    if n % 2:
        mid = power_self(a, n // 2)
        return (mid**2) * a
    else:
        mid = power_self(a, a // 2)
        return mid**2


if __name__ == '__main__':
    start = time()
    result = power_self(2, 20)
    end = time() - start
    print(result, end)