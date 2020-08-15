#all prime num
num = 20
p = []
for i in range(2,20):
    div = int(i/2)+1
    t = True
    for x in range(2,div):
        if i%x == 0:
            t = False
    if t == True:
        p.append(i)
print(p)
t = 1
for x in p:
    t *= x
print(t)
