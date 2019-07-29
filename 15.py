from random import random

array = []

for i in range(10):
    temp = [int(random()*10) for j in range(10)]
    array.append(temp)
for x in array:
    print(x)

sum_diagonals1 = 0
sum_diagonals2 = 0

for i in range(10):
    sum_diagonals1 += array[i][i]
    sum_diagonals2 += array[i][len(array[i])-i-1]

print(sum_diagonals1, " and ", sum_diagonals2)