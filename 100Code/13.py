from random import randint

array = []

for x in range(10):
    y = []
    for j in range(10):
        y.append(randint(1,50))
    array.append(y)

for i in array:
    for j in i:
        print("%2d" % j, end=" ")
    print("")

#sakht o namayeshe matrix 2bodi