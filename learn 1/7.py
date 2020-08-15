num = 0
p =[]
i=2
k = 0
while i<500:
    div = int(i/2)+1
    t = True
    for x in range(2,div):
        if i%x == 0:
            t = False
            continue
    if t == True:
        p.append(i)
        k = k + 1
        print(k , i)
    i = i+ 1
print(sum(p))
