def find_jewelry(j, s):
    target = set(j)
    count = 0
    for i in s:
        if i in target:
            count += 1
    print(count)

if __name__ == '__main__':
    j = 'aA'
    s = 'aAAbbb'
    find_jewelry(j, s)