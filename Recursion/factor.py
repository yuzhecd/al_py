def factorial(m):
    n = 1
    for i in range(1, m + 1):
        n *= i
    return n

def factorical_recursive(m):
    if m == 0:
        return 1
    else:
        return m * factorical_recursive(m-1)

if __name__ == '__main__':
    m = int(input('Please input a interger: '))
    result_a = factorial(m)
    result_b = factorial(m)
    print(result_a,result_b)
