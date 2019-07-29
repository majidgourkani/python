from random import randint

array = []
row  = 5
col = 10
for i in range(row):
    temp = [int(randint(1,40)+10) for j in range(col)]
    array.append(temp)
for x in array:
    print(x)

num = int(input("insert your number: "))

print("Rows: ", end=" ")
for x in range(row):
    if num in array[x]:
        print(x+1, end=" ")

print()
print("Columns: ", end=" ")
for i in range(col):
    for j in range(row):
        if array[j][i] == num:
            print(i+1, end=" ")
            break
