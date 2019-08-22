import random 
M = [[None] * 9 for i in range(9)]

p = 0.05

for i in range(9):
    for j in range(9):
        M[i][j] = 0 if random.random() < p else 1

for x in M:
    print(x)

M_row = []
M_column = []
for i in range(9):
    for j in range(9):
        if M[i][j] == 0:
            if i not in M_row:
                M_row.append(i)
            if j not in M_column:
                M_column.append(j)

for i in range(9):
    for j in range(9):
        if (i in M_row or j in M_column):
            M[i][j] = 0

print()
for x in M:
    print(x)
