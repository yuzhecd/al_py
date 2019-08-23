def subset2(num):
    mid_result = []
    result = []
    subset2_helper(num, mid_result, result, 0)
    print(result)

def subset2_helper(num, mid_result, result, position):
    result.append(mid_result[:])
    for i in range(position, len(num)):
        mid_result.append(num[i])
        subset2_helper(num, mid_result, result, i + 1)
        mid_result.pop()

if __name__ == '__main__':
    subset2([1, 2, 3])