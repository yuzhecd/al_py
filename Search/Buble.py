def bubll(alist):
    for i in range(len(alist)):
        for j in range(1, len(alist) - i):
            if alist[j-1] > alist[j]:
                alist[j-1], alist[j] = alist[j], alist[j-1]

    return alist

if __name__ == '__main__':
    alist = [2, 1, 7, 5, 4, 10, 9]
    r = bubll(alist)
    print(r)
