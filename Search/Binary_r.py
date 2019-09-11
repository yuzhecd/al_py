def binary_recirle(alist):
    if len(alist) == 0:
        return -1

    left, right = 0, len(alist) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if alist[mid] < alist[right] and alist[mid] > alist[left]:
            return alist[left]
        elif alist[mid] > alist[right] and alist[mid] > alist[left]:
            left = mid + 1
        elif alist[mid] < alist[right] and alist[mid] < alist[left]:
            right = mid
        else:
            return -2

    if alist[left] < alist[right]:
        return alist[left]
    else:
        return alist[right]

    return -3

if __name__ == '__main__':
    alist = [5, 1, 2, 3, 4 ]
    result = binary_recirle(alist)
    print(result)