def binary_flow(alist, target):
    left, right = 0, 1

    while alist[right] < target:
            left = right
            right *= 2
            if right >= len(alist):
                right = len(alist) - 1
                break

    while left + 1 < right:
        mid = left + (right - left) // 2
        if alist[mid] == target:
            right = mid
        elif alist[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return (left, alist[left]) if alist[left] == target else (right, alist[right])

if __name__ == '__main__':
    alist = [1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,4,4,5,6,6,6,6, 7, 9]
    result = binary_flow(alist, 9)
    print(result)
