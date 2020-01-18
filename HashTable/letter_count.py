from collections import Counter

def count_letter(s, k):
    result = {}
    for l in s:
        result[l] = 1 + result.get(l, 0)
    print(result)

    result_k = []
    sorted_value = sorted(result.values(), reverse=True)
    target = sorted_value[k-1]
    for key, element in result.items():
        if element >= target:
            result_k.append([key, element])
    print(result_k)

def count_counter(s):
    c = Counter(s)
    print(c.most_common(2))

if __name__ == "__main__":
    s = "hhhyeser"
    count_letter(s, 2)
    count_counter(s)