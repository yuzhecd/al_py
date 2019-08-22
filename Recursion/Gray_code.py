def grad_code(n, boolean):
    if n == 0:
        return 
    grad_code(n-1, True)
    print('enter  ', n ) if boolean else print('exit   ', n)
    grad_code(n-1, False)

    
if __name__ == '__main__':
    grad_code(5, True)
