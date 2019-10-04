def egg_min(floors, target):
    for i in range(floors):
        if i * (i + 1) >= 2 * floors:
            x = i
            break
    first_egg = True
    floor_f = x
    print(floor_f)
    i = 1
    while first_egg == True:
        if floor_f == target:
            return i
        elif floor_f > target:
            first_egg = False
        else:
            floor_f += x - i
            print(floor_f)
            i += 1 
    
    for j in range(floor_f -x + i, target+1):
        print(j)
    
    return target - (floor_f - x + i - 1) + i

if __name__ == '__main__':
    result = egg_min(100, 76)
    print(result)
     