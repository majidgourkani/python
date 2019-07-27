from random import randint

x = [int(randint(1,50)) for i in range(30)]
print(x)

j = len(x) - 1

while j != 0:
    k = 0
    for i in range (1,j+1):
        if x[i] > x[k]:
            k = i
    temp = x[k]
    x[k] = x[j]
    x[j] = temp
    j -= 1

print(x)