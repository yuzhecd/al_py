def find_rev(alist):
    num = 0
    for i in range(len(alist)):
        for j in range(i+1, len(alist)):
            if alist[i] > alist[j]:
                num += 1
                print(num, (alist[i], alist[j]))


if __name__ == '__main__':
    number = [1, 9, 2, 7, 4, 8, 5]
    find_rev(number)