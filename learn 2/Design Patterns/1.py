list = [1,2,3,4,5]
for i in list:
    print(i)
iter = list.__iter__()
print("")
print(iter.__next__())
print(iter.__next__())
print(iter.__next__())
print("******************")

num = [1,2,3,4,5,6,7]
copy_num = [n for n in num]
print(copy_num)
even_num = [n for n in num if n%2 == 0]
print(even_num)
ood_squr = [n**2 for n in num if n%2 == 1]
print(ood_squr)

matrix = [[1,2,3], [4,5,6], [7,8,9]]
flat = [n for row in matrix for n in row]
print(flat)
print("******************")
