def subset(nums):
    result = [[]]
    for num in range(1, nums + 1):
        for element in result[:]:
            mid = element[:]
            mid.append(num)
            result.append(mid)
    print(result)

def subset_recursion(nums):
    mid_result = []
    result = []
    subset_recursion_helper(nums, mid_result, result, 0)
    print(result)

def subset_recursion_helper(nums, mid_result, result, position):
    result.append(mid_result[:])
    for i in range(position, len(nums)):
        mid_result.append(nums[i])
        subset_recursion_helper(nums,mid_result, result, i+1)
        mid_result.pop()


if __name__ == '__main__':
    subset_recursion([1, 2, 3])