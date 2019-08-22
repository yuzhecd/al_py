def matrix_pro(M):
    row = len(M)
    column = len(M[0])

    for i in range(row):
        result_row = result_column = result_blk = 0
        for j in range(column):
            tmp = M[i][j]
            if result_row & (1 << (tmp - 1)) == 0:
                result_row = (result_row | (1 << (tmp - 1)))
            else:
                print('False position:{},{}, number:{}'.format(i, j, tmp))
                return False

            tmp = M[j][i]
            if result_column & (1 << (tmp - 1)) == 0:
                result_column = (result_column | (1 << (tmp - 1)))
            else:
                print('False position:{},{}, number:{}'.format(j, i, tmp))
                return False

            p = (i // 3) * 3 + j // 3
            q = (i % 3) * 3 + j % 3
            tmp = M[p][q]
            if result_blk & (1 << (tmp - 1)) == 0:
                result_blk = (result_blk | (1 << (tmp - 1)))
            else:
                print('False block:{}, number:{}'.format(i, tmp))
                return False
    return True

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
    output = matrix_pro(matrix)
    print(output)