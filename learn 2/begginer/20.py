name = ["one" , "two" , "three" , "for" , "five" , "six"]
indes = 0
while indes < len(name):
    print(name[indes])
    indes = indes + 1

while True:
    print("enter a and b that a + b = 20")
    a , b = int(input("a:")) , int(input("b:"))
    if a+b == 20:
        print("a + b = {:d}".format(a+b))
        break
    else:
        print("{:d}, enter other number.".format(b+a))
