def find_kmax(alist, target):

    pivot = alist[0]
    left = [x for x in alist if x < pivot]
    right = [x for x in alist if x > pivot]
    if len(left) + 1 == target:
        return pivot
    elif len(left) + 1 < target:
        return find_kmax(right, target-len(left)-1)
    else:
        return find_kmax(left, target)

if __name__ == '__main__':
    example = [4, 2, 6, 5, 7, 1, 8, 3]
    result = find_kmax(example, 7)
    print(result)