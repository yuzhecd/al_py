from time import time
def bubll(alist):
    start = time()
    for i in range(len(alist)):
        for j in range(1, len(alist) - i):
            if alist[j-1] > alist[j]:
                alist[j-1], alist[j] = alist[j], alist[j-1]
    end = time() - start

    return alist, end

def buble_improve(alist):
    start = time()
    for i in range(len(alist)):
        is_sorted = True
        for j in range(1, len(alist)-i):
            if alist[j-1] > alist[j]:
                alist[j-1], alist[j] = alist[j], alist[j-1]
                is_sorted = False
        if is_sorted == True: break
    end = time() - start
    return alist, end


if __name__ == '__main__':
    alist = [2, 1, 7, 5, 4, 10, 9]
    r, r_t= bubll(alist)
    i, i_t = buble_improve(alist)
    print(r, r_t)
    print(i, i_t)
