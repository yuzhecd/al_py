def find_remerge(alist):
    if len(alist) == 1:
        return alist, 0
    m = len(alist) // 2
    left, count_l = find_remerge(alist[:m])
    right, count_r = find_remerge(alist[m:])

    return _merge(left, right, count_l + count_r)

def _merge(left, right, count):
    temp = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            for k in range(i, len(left)):
                print(left[k], right[j])
                count += 1
            temp.append(right[j])
            j += 1
        else:
            temp.append(left[i])
            i += 1
    if i != len(left):
        temp += left[i:]
    else:
        temp += right[j:]
    return temp, count

if __name__ == '__main__':
    alist_a = [9, 4, 1, 6, 3, 5, 7]
    alist_b = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    result, num = find_remerge(alist_a)
    print(result, num)