def sqrt_my(x):
    if x == 0:
        return x
    left, right = 0, x
    while left <= right:
        mid = left + (right - left) // 2
        if mid == x // mid:
            return mid
        elif mid < x // mid:
            left = mid + 1
        else:
            right = mid - 1
    return right

if __name__ == '__main__':
    result = sqrt_my(29)
    print(result)