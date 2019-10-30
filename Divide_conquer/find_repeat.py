def find_repeat(list_a, list_b):
    i, j = 0, 0
    while i < len(list_a) and j < len(list_b):
        if list_a[i] != list_b[j]:
            return list_a[i] if list_a[i] < list_b[j] else list_b[j]
        else:
            i += 1
            j += 1
    return list_a[i] if j == len(list_b) else list_b[j] 


if __name__ == '__main__':
    a = [1, 3, 5, 6, 8, 9]
    b = [1, 3, 5, 8, 9]
    result = find_repeat(a, b)
    print(result)