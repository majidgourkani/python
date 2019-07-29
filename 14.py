from random import random

array = []

for i in range(10):
    temp = [int(random()*10) for j in range(10)]
    array.append(temp)
for x in array:
    print(x)

rowmax = 0
row = 0
itrt = 0

for x in array:
    if rowmax < sum(x):
        rowmax = sum(x)
        row = itrt
    itrt += 1
print()
print("Max row sum: sum of row %d is %d" % (row, rowmax))

colmax = 0
col = 0

for x in range(10):
    colsum = 0
    for y in range(10):
        colsum += array[x][y]
    if colmax < colsum:
        colmax = colsum
        col = y
print()
print("Max column sum: sum of column %d is %d" % (col, colmax))