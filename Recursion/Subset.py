def subset(nums):
    result = [[]]
    for num in range(1, nums + 1):
        for element in result[:]:
            mid = element[:]
            mid.append(num)
            result.append(mid)
    print(result)

def subset_recursion(num):
    mid_result = []
    result = []
    subset_recursion_helper(num, mid_result, result, 0)
    print(result)

def subset_recursion_helper(num, mid_result, result, position):
    # have a copy!
    result.append(mid_result[:])
    for i in range(position, len(num)):
        mid_result.append(num[i])
        subset_recursion_helper(num, mid_result, result, i+1)
        # backing
        mid_result.pop()

def subset_recursion_duplicate(num):
    mid_result = []
    result = []
    num.sort()
    subset_recursion_duplicate_helper(num, mid_result, result, 0)
    print(result)

def subset_recursion_duplicate_helper(num, mid_result, result, position):
    result.append(mid_result[:])
    for i in range(position, len(num)):
        if num[i-1] == num[i]:
            continue
        mid_result.append(num[i-1])
        subset_recursion_duplicate_helper(num, mid_result, result, i+1)
        mid_result.pop()

if __name__ == '__main__':
    subset_recursion([1, 2, 3])
    subset_recursion_duplicate([1,1,1,1,2,3,3])