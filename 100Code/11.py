from random import randint

x = [int(randint(1,50)) for i in range(30)]
print(x)


for i in range(30):
    for j in range(len(x)-i-1):
        if x[j] > x[j+1]:
            temp = x[j]
            x[j] = x[j+1]
            x[j+1] = temp

print(x)

#sort kardan ye array