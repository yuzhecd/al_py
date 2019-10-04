from time import time
def _quick_sort(alist):
    if len(alist) <= 1:
        return alist

    pivot = alist[0]
    left = _quick_sort([x for x in alist[1:] if x <= pivot])
    right = _quick_sort([x for x in alist[1:] if x > pivot])
    return left + [pivot] + right

def quick_sort(alist):
    start = time()
    result = _quick_sort(alist)
    end = time() - start
    print(result, end)

if __name__ == '__main__':
    nums = [5, 2, 1, 9, 7, 8, 4]
    quick_sort(nums)