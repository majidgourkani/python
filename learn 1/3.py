num = 600851475143
t = 2

while t<num:
    if num%t == 0:
        num = num/t
    t +=1
print(t)
