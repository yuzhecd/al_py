def perm_size(result, nums, k):
    if k == 0:
        print(result)
    for i in range(len(nums)):
        perm_size(result + str(nums[i]),nums[:i] + nums[i+1:], k-1)

if __name__ == '__main__':
    nums=[1,2,3,4,5]
    perm_size('', nums, 3)