import random

array = {1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f"}

print(array)

keylist = list(array.keys())
del_key = random.choice(keylist)
del array[del_key]

print("deleted key is: ", del_key)
print(array)

#hazf yek key az yek dictionary