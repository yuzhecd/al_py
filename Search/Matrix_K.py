def matrix_kmax(matrix, k):
    row = len(matrix)
    col = len(matrix[0])

    maxofrow = [col - 1] * row

    r = 0

    for i in range(k):
        max_number = matrix[0][0]
        for j in range(row):
            if maxofrow[j] > -1:
                if max_number < matrix[j][maxofrow[j]]:
                    max_number = matrix[j][maxofrow[j]]
                    r = j

        maxofrow[r] -= 1

    return max_number

if __name__ == '__main__':
    example = [[1, 2, 3, 4], [2, 5, 7, 9], [3, 6, 11, 18], [22, 24, 36, 45]]
    result = matrix_kmax(example, 2)
    print(result)