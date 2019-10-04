import numpy as np 

def matrix_fibonacci(n):
    base = np.array([[1,1], [1, 0]])
    sum_all = np.array([[1, 0], [0, 1]])
    while n != 0:
        if (n & 1) == 1:
            sum_all = np.dot(sum_all, base)
        base = np.dot(base, base)
        n = n >> 1
    return sum_all[0][1]



if __name__ == '__main__':
    result = matrix_fibonacci(6)
    print(result)