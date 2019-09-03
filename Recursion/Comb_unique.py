def comb(nums, target):
    mid_result = []
    result = []
    nums.sort()
    comb_helper(nums, mid_result, result, target, 0)
    print(result)
    
def comb_helper(nums, mid_result ,result, remains, position):
    if remains < 0:
        return 
    if remains == 0:
        result.append(mid_result[:])
        
    for i in range(position, len(nums)):
        if (i > position and nums[i] == nums[i-1]): 
            continue
        mid_result.append(nums[i])
        comb_helper(nums, mid_result, result, remains-nums[i], i+1)
        mid_result.pop()

if __name__ == '__main__':
    nums = [10, 1, 2, 7, 6, 1, 5]
    t = 8
    comb(nums, t)
