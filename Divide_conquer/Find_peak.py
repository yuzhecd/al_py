def find_peak(alist):
    left, right = 0, len(alist) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if alist[mid-1] < alist[mid] and alist[mid] > alist[mid+1]:
            return alist[mid]
        elif alist[mid-1] > alist[mid] and alist[mid] > alist[mid+1]:
            right = mid - 1
        else:
            left = mid + 1

    if left == right:
        return alist[left]
    if left + 1 == right:
        if alist[left] > alist[right]:
            return alist[left]
    return "not found"

if __name__ == '__main__':
    example = [float('inf'), 3, 4, 9, 14, 25, 7, 6, 5, float('inf')]
    result = find_peak(example)
    print(result)


