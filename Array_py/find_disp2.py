def find_dispeared2(n):
    for i in range(len(n)):
        index = abs(n[i]) - 1
        n[index] = -abs(n[index]) 

    return [i + 1 for i in range(len(n)) if n[i] > 0]


if __name__ == '__main__':
    num = [2, 3, 1, 1, 5 , 7, 5]
    result = find_dispeared2(num)
    print(result)