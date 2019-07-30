from random import random

array = []

for i in range(50):
  array.append(int(random()*1000))

array.sort()
print(array)

num = int(input("insert your number: "))

mini = 0
maxi = len(array) - 1

while mini <= maxi:
  mid = (mini + maxi) // 2
  if num == array[mid]:
    print("num finded, "+str(array[mid])+ " is in index: "+str(mid))
    break
  elif num < array[mid]:
    maxi = array.index(array[mid]) - 1
  else:
    mini = array.index(array[mid]) + 1 
else:
  print("ther is no number....")

print("have a good time")

#bazi peyda kardan adad