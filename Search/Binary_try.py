def binary_search(nums, target):
    nums.sort()
    left = 0
    right = len(nums)-1
    return binary_search_helper(nums, target, left, right)

def binary_search_helper(nums, target, left, right):
    if left > right:
        #print('-1')
        return -1
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search_helper(nums, target, mid+1, right)
    else:
        return binary_search_helper(nums, target, left, mid-1)

if __name__ == '__main__':
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    result = binary_search(nums, 5)
    print(result)
