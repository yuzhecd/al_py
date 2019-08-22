import math
def Sudocu(n):
    length =  int(math.sqrt(n))
    M = [[None] * length for i in range(length)]
    M[length - 1][length // 2] = 1
    p = length -1
    q = length // 2 
    for i in range(2, n + 1):
        p += 1
        q += 1
        p = p % length
        q = q % length
        if M[p][q] == None:
            M[p][q] = i
        else:
            p -= 2
            q -= 1
            M[p][q] = i
    for i in M:
        print(i)

if __name__ == '__main__':
    Sudocu(25)
            