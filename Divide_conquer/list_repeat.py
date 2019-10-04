def find_same(list_a, list_b):
    list_a.sort()
    list_b.sort()

    i, j = 0, 0
    result = []
    while i < len(list_a) and j < len(list_b):
        if list_a[i] == list_b[j]:
            result.append(list_a[i])
            i += 1
            j += 1
        elif list_a[i] > list_b[j]:
            j += 1
        else:
            i += 1

    return result 

if __name__ == '__main__':
    a = [4, 2, 1, 2, 3, 3, 5]
    b = [9, 8 ,1, 3, 3, 3, 2, 2]
    result = find_same(a, b)
    print(result)