def num_max(n):
    max = mid = 0
    for i in n:
        if i > max:
            mid = max
            max = i
        elif i > mid:
            mid = i
    if ((max // mid) >= 2):
        return True
    else:
        return False

if __name__ == '__main__':
    num = [1, 2, 3, 4, 10, 33, 15, 6, 8 ,22 , 55, 38]
    result = num_max(num)
    print(result)