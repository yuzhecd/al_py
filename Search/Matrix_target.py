def find_target(matrix, target):
    i, j = len(matrix) - 1, 0

    while i >= 0 and j <= len(matrix[0])- 1:
        if matrix[i][j] == target:
            return (i, j, target)
        elif matrix[i][j] < target:
            j += 1
        else:
            i -= 1
    return "not found"

if __name__ == '__main__':
    example = [[1, 2, 3, 4], [2, 5, 7, 9], [3, 6, 11, 18], [22, 24, 36, 45]]
    result = find_target(example, 6)
    print(result)