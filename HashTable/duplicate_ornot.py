def have_duplicate(s):
    print(len(s) > len(set(s)))

def have_duplicate_in_k(s, k):
    dict1 = {}
    for i, element in enumerate(s):
        if element not in dict1:
            dict1[element] = i
        else:
            if (i - dict1[element]) <= k:
                return True
            else:
                dict1[element] = i
    return False

if __name__ == "__main__":
    s1 = [1, 2, 3, 4, 5]
    s2 = [1, 2, 3, 4, 5, 3]
    have_duplicate(s2)
    print(have_duplicate_in_k(s2, 3))