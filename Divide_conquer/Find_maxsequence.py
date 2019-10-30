from time import time
#O(n^3)
def find_m(alist):
    start = time()
    global_max = 0
    for i in range(len(alist)):
        local_max = 0
        for j in range(i, len(alist)):
            sum = 0
            for k in range(i, j+1):
                sum += alist[k]
            local_max = local_max if local_max > sum else sum
        global_max = local_max if local_max > global_max else global_max
    end = time() - start
    return (global_max, end)

#O(n^2)
def find_m2(alist):
    start = time()
    global_max = 0
    for i in range(len(alist)):
        local_max, sum = 0, 0
        for j in range(i, len(alist)):
            sum += alist[j]
            local_max = sum if sum > local_max else local_max
        global_max = local_max if local_max > global_max else global_max
    end = time() - start
    return (global_max, end)

#O(nlogn)
def find_m3(alist):
    if len(alist) == 1:
        return max(alist[0], 0)

    mid = 0 + (len(alist) - 0) // 2
    left_max = find_m3(alist[:mid])
    right_max = find_m3(alist[mid:])
    max_leftright = max(left_max, right_max)

    sum_a, max_leftborder= 0, 0
    for i in range(mid, -1, -1):
        sum_a += alist[i]
        max_leftborder = sum_a if sum_a > max_leftborder else max_leftborder

    sum_b, max_rightborder = 0, 0
    for j in range(mid+1, len(alist)):
        sum_b += alist[j]
        max_rightborder = sum_b if sum_b > max_rightborder else max_rightborder
    return max(max_leftright, max_leftborder+max_rightborder)

#O(n)
def find_m4(alist):
    local_max = alist[0]
    global_max = 0
    for i in range(1, len(alist)):
        local_max += alist[i]
        local_max = max(alist[i], local_max)
        global_max = max(local_max, global_max)
    return global_max


if __name__ == '__main__':
    a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    start = time()
    result_1 = find_m(a)
    end_1 = time() - start
    start = time()
    result_2 = find_m2(a)
    end_2 = time() - start
    start = time()
    result_3 = find_m3(a)
    end_3 = time() - start
    start = time()
    result_4 = find_m4(a)
    end_4 = time() - start
    print(result_1, result_2, result_3, result_4, end_1, end_2, end_3, end_4)