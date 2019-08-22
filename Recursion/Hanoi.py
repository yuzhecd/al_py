def hanoi(n, a, b, c):
    if n == 1:
        print('Move {} to {}'.format(a, b))
    else:
        hanoi(n-1, a, b, c)
        hanoi(1, a, c, b)
        hanoi(n-1, b, c, a)

if __name__ == '__main__':
    result = hanoi(5, 'start', 'by', 'end')
    print(result)
    

