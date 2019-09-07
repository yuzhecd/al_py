def _merge_sort(alist):
    if len(alist) == 1:
        return alist
    m = len(alist) // 2
    left = _merge_sort(alist[:m])
    right = _merge_sort(alist[m:])
    return _merge(left, right)

def _merge(left, right):
    i, j = 0, 0
    temp = []
    len_l = len(left)
    len_r = len(right)
    while i < len_l and j < len_r:
        if left[0] < right[0]:
            temp.append(left[0])
            left.pop(0)
            i += 1
        else:
            temp.append(right[0])
            right.pop(0)
            j += 1
    if len(left) != 0:
        temp += left
    else:
        temp += right
    return temp

def merge_sort(alist):
    return _merge_sort(alist)

if __name__ == '__main__':
    alist = [9, 4, 1, 6, 3, 4, 7]
    result = merge_sort(alist)
    print(result)

