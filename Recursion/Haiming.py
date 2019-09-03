def haiming(alist, n):

    def haiming_helper(result, nums, k, length):
        if k == 0:
            print(result)

        for i in range(len(nums)):
            result_copy = result[:]
            result_copy[length-len(nums)+i] = 0 if nums[i] == 1 else 1
            haiming_helper(result_copy, nums[i+1:], k-1, length)

    haiming_helper(alist, alist, n, len(alist))

if __name__ == '__main__':
    alist = [0, 0, 0, 0]
    haiming(alist,2)