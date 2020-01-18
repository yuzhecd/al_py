def find_intersection(a, b):
    print(set(a) & set(b))

def find_dup_intersection(a, b):
    dict1 = {}
    for i in a:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] += 1

    result = []
    for i in b:
        if i in dict1 and dict1[i] > 0:
            result.append(i)
            dict1[i] -= 1
    print(result)

if __name__ == '__main__':
    a = [1, 2, 2, 1]
    b = [2, 2]
    find_intersection(a, b)
    find_dup_intersection(a, b)
