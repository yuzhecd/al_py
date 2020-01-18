def find_unique(s):
    result = {}
    for c in s:
        result[c] = 1 + result.get(c, 0)
    
    for letter, value in result.items():
        if value == 1:
            print(letter, end=' ')
    print()

def find_unique_counter(s):
    result = [l for l in s if s.count(l) == 1]
    print(result)

if __name__ == '__main__':
    s = 'aabcdddef'
    find_unique(s)
    find_unique_counter(s)