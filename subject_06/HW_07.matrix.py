from random import randrange

N = 10
matrix = [[randrange(0, 10) for i in range(N)] for j in range(N)]
for row in matrix:
    print(row)
