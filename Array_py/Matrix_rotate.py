
def matrix_ro(n):
    matrix = [[i + j for i in range(1, n + 1)] for j in range(0, n*(n-1) + 1, n)]
    for i in matrix:
        print(i)
    print()

    rotate_matrix = [[None for i in range(n)] for j in range(0, n*(n-1) + 1, n)] 
    for i in range(n):
        for j in range(n):
            rotate_matrix[n -1- i][j] = matrix[j][i]

    for i in rotate_matrix:
        print(i)

if __name__ == '__main__':
    matrix_ro(4)