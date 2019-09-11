def binary_findsection(alist, target):
    if len(alist) == 0:
        return -1
    left, right = 0, len(alist) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if alist[mid] == target:
            right = mid 
        elif alist[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    if alist[left] == target:
        section_left = left
    elif alist[right] == target:
        section_left = right
    else:
        return (-1, -1)

    left, right = 0, len(alist) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if alist[mid] == target:
            left = mid 
        elif alist[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    if alist[right] == target:
        section_right = right
    elif alist[left] == target:
        section_right = left
    else:
        return (-2, -2)
    
    return (section_left, section_right)


if __name__ == '__main__':
    alist = [1, 1, 2, 2, 2, 2, 3, 4]
    result = binary_findsection(alist, 3)
    print(result)