def plus_nu(m):
    i = len(m) - 1
    while i >= 0:
        if m[i] != 9:
            m[i] += 1
            break
        else:
            m[i] = 0
            if i != 0:
                i -= 1
            else:
                m.insert(0, 1)
                break
    print(m)

if __name__ == '__main__':
    num = [1,9,9]
    plus_nu(num)