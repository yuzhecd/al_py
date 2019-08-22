import random
def mine(m, n, p):
    z = [[0] * (m + 2) for i in range(n + 2)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if random.random() <= p:
                z[i][j] = -1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            print('*', end=' ') if z[i][j] == -1 else print(z[i][j], end=' ')
        print()
    
    print()
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if z[i][j] == -1:
                for p in range(-1, 2):
                    for q in range(-1, 2):
                        if z[i+p][j+q] != -1:
                            z[i+p][j+q] += 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            print('*', end=' ') if z[i][j] == -1 else print(z[i][j], end=' ')
        print()
if __name__ == '__main__':
    mine(10, 10, 0.2)
