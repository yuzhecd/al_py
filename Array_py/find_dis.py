def find_dispearednu(n):
    result = []
    for i in range(1, len(n)+1):
        if i not in n:
            result.append(i)

    print(result)

if __name__ == '__main__':
    num = [2, 3, 1, 1, 5 , 7, 5]
    find_dispearednu(num)