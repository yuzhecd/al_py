def max_find(num):
    local = maximum = 0
    for i in num:
        local = local + 1 if i == 1 else 0
        maximum = max(local, maximum)

    print(maximum)

if __name__ == '__main__':
    num = [1,1,1,1,0,1,1,0,1,1,1,1,1,1,1]
    max_find(num)