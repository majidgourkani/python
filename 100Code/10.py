from random import random

x = [int(random()*10) for i in range(50)]
print(x)

maxfrqnc  = 0
temp = 0
num = -1

for item in x:
    temp = x.count(item)
    if temp > maxfrqnc:
        maxfrqnc = temp
        num = item

print("item %d repeted %d times in array" % (num,maxfrqnc))

#peyda kardan por tekrar tarin item ye array