def select_sort(alist):
    for i in range(len(alist)):
        min_index = i
        for j in range(i, len(alist)):
            if alist[min_index] > alist[j]:
                min_index = j
        alist[min_index], alist[i] = alist[i], alist[min_index]

    return alist

if __name__ == '__main__':
    alist = [2, 1, 7, 5, 4, 10, 9]
    result = select_sort(alist)
    print(result)