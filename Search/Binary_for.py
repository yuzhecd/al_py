def binary_for(alist, item):
    left, right = 0, len(alist) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if alist[mid] == item:
            return mid
        elif alist[mid] > item:
            right = mid - 1 
        else:
            left = mid + 1
    return "Not found"

if __name__ == '__main__':
    alist = [1, 2, 3, 4, 5, 6]
    item = 7
    result = binary_for(alist, item)
    print(result)