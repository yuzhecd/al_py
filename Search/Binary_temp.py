def binary_temple(alist, target):
    if len(alist) == 0:
        return -1

    left, right = 0, len(alist) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if alist[mid] == target:
            right = mid
        elif alist[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if alist[left] == target:
        return left, alist[left]
    if alist[right] == target:
        return right, alist[right]

    return -1

if __name__ == '__main__':
    alist = [1, 2, 2, 2, 3, 4, 4, 4, 8, 9]
    result = binary_temple(alist, 2)
    print(result)