def comb(nums, remains):
    temp = []
    result = []

    def comb_helper(nums, temp, result, remains, position):
        if remains < 0:
            return
        if remains == 0:
            result.append(temp[:])

        for i in range(position, len(nums)):
            #mid_result = temp[:]
            temp.append(nums[i])
            comb_helper(nums, temp, result, remains-nums[i], i)
            temp.pop()

    comb_helper(nums, temp, result, remains, 0)
    print(result)

if __name__ == '__main__':
    nums = [2, 3, 7, 9]
    num = 9
    comb(nums, num)
