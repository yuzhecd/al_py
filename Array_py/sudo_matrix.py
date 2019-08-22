def matrix_verification(M):
    p = len(M)
    q = len(M[0])

    for i in range(p):
        if sum(M[i]) != 45:
            return "This is not a matrix, error 1"
    
    for j in range(q):
        if sum(M[:][j]) != 45:
            return "This is not a matrix, error 2"

    t = 0
    for r in range(3):
        for s in range(3):
            t = 0
            for i in range(3):
                for j in range(3):
                    t += M[i+3*r][j+3*s]
            if t !=45:
                return "This is not a matrix, error 3"
    return 'EXCELLENT'

if __name__ == '__main__':
    matrix = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]
]
    output = matrix_verification(matrix)
    print(output)