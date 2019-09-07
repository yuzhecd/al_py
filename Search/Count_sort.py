from time import time
def count_sort(alist):
    start = time()
    max_num, min_num = alist[0], alist[0]
    for i in range(len(alist)):
        if alist[i] < min_num:
            min_num = alist[i]
        if alist[i] > max_num:
            max_num = alist[i]

    mid_list = [0]*(max_num - min_num + 1)
    
    for i in alist:
        mid_list[i-min_num] += 1

    pos = 0
    for i in range(len(mid_list)):
        for j in range(mid_list[i]):
            alist[pos] = i + min_num
            pos += 1
    end = time() - start
    print(alist, end)

if __name__ == '__main__':
    nums = [12, 3, 9, 0, 9, 8, 7, 7, 2]
    count_sort(nums)