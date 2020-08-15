valu = int(input("all the prime number checker\nenter a number: "))
for x in range(2 , valu):
    mid = int(x / 2) + 1
    count = True
    for y in range(2,mid):
        if x%y == 0:
            count = False
            continue
    if count == True:
        print(str(x)+" is prime")
#######################################################################
valu = int(input("prime number checker\nenter a number: "))
if valu >=2 :
    divs = []
    for div in range(2,int(valu/2)+1):
        if valu % div == 0:
            divs.append(div)
    if len(divs) == 0:
        print("{:d} is prime".format(valu))
    else:
        print("{:d} is not prime, becuse is divided to {:}.".format(valu, str(divs)))
else:
    print("{:d} is not prime".format(valu))
