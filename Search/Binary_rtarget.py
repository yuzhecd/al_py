def Binary_targetr(alist, target):
    if len(alist) == 0:
        return -1
    
    left, right = 0, len(alist) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if alist[mid] == target:
            return mid, alist[mid]
        elif alist[mid] < alist[right] and alist[mid] > alist[left]:
            if alist[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        elif alist[mid] > alist[left] and alist[mid] > alist[right]:
            if alist[left] <= target and alist[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        elif alist[mid] < alist[left] and alist[mid] < alist[right]:
            if alist[mid] < target and alist[right] >= target:
                left = mid + 1
            else:
                right = mid - 1
        else:
            return -2

    if alist[left] == target:
        return left, alist[left]
    if alist[right] == target:
        return right, alist[right]

    return -3

if __name__ == '__main__':
    alist = [5, 6, 7, 1, 2, 3, 4]
    result = Binary_targetr(alist, 2)
    print(result)
