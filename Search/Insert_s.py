from time import time
def insert_sort(alist):
    start = time()
    for sorted in range(len(alist)):
        un_sort = sorted
        while un_sort > 0 and alist[un_sort-1] > alist[un_sort]:
            alist[un_sort-1], alist[un_sort] = alist[un_sort], alist[un_sort-1]
            un_sort -= 1
    end = time() - start
    print(alist, end)

if __name__ == '__main__':
    nums = [5, 1, 3, 2, 6, 4]
    insert_sort(nums)
