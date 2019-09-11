def binary_searchp(alist, target):
    if len(alist) == 0:
        return -1
    left, right = 0, len(alist) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if alist[mid] == target:
            return mid
        elif alist[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    if alist[left] >= target:
        return left
    if alist[right] >= target:
        return right
    return right + 1

if __name__ == '__main__':
    alist = [2, 4, 5, 8, 9, 11, 14, 18]
    result = binary_searchp(alist, 19)
    print(result)