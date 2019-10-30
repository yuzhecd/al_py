#O(n^2)
def change_order(alist):
    m = len(alist) // 2
    for i in range(0, m-1):
        s = i + m
        for j in range(s, s-(m-1-i),-1):
            alist[j], alist[j-1] = alist[j-1], alist[j]
    return alist

#O(nlgn)
def change_orderfast(alist):
    mid = len(alist) // 2
    if mid == 1:
        return alist

    mid2 = mid // 2
    for i in range(mid2, mid):
        alist[i], alist[i+mid2] = alist[i+mid2], alist[i]
    left = change_orderfast(alist[:mid])
    right = change_orderfast(alist[mid:])
    return left + right

# class method O(nlgn)
def  shuffleArray(a, left ,right):
    if (right - left) == 1:
        return 

    mid = (left + right) // 2
    temp = mid + 1
    mmid = (left + mid) // 2

    for i in range(mmid+1, mid+1):
        (a[i], a[temp]) = (a[temp], a[i])
        temp += 1

    shuffleArray(a, left, mid)
    shuffleArray(a, mid+1, right)
    print(a)

if __name__ == '__main__':
    result_slow = change_order([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
    result_fast = change_orderfast([1, 2, 3, 4, 5, 6, 7, 8])
    print(result_slow)
    print(result_fast)
    # have some problems！
    #shuffleArray([1, 2, 3, 4, 5, 6], 0, 5)

