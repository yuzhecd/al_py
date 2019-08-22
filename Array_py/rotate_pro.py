def rotate_inplace(n):
    matrix = [[i + j for i in range(1, n+1)] for j in range(0, n*(n - 1) + 1, n)]
    for i in matrix:
        print(i)
    print()

    layer = n // 2
    for i in range(layer):
        first = i
        last = n - 1 - i 
        for j in range(first, last):
            offset = j - first
            buffer = matrix[first][j]

            #left -> top
            matrix[first][j] = matrix[last - offset][first]

            #bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]

            #right -> bottom
            matrix[last][last - offset] = matrix[j][last]

            #top -> right
            matrix[j][last] = buffer
    
    for i in matrix:
        print(i)
    print()

    for i in range(layer):
        first = i
        last = n - 1 - i
        for j in range(first, last):
            offset = j - first
            buffer = matrix[first][j]

            #right -> top
            matrix[first][j] = matrix[j][last]

            #bottom -> right
            matrix[j][last] = matrix[last][last - offset]

            #left -> bottom
            matrix[last][last - offset] = matrix[last - offset][first]

            #top -> left
            matrix[last - offset][first] = buffer

    for i in matrix:
        print(i)

if __name__ == '__main__':
    rotate_inplace(4)