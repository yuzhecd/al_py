def fabonacci(m):
    if m == 1 or m == 2:
        return 1
    return fabonacci(m-1) + fabonacci(m-2)

def fabonacci2(m):
    if m <= 1:
        return (m, 0)
    a,b = fabonacci2(m-1)
    return (a+b, a)

def fabonacci3(m):
    a = 1
    b = 0
    for i in range(m-1):
        a, b = a+b, a
    return(a)

if __name__ == '__main__':
    m = int(input('Please input a interger: '))
    result = fabonacci3(m)
    print(result)