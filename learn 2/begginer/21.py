#print(dir(memoryview))
import sys

val = input()
var = val.split()
if len(var) != 3:
    print("wrong format")
    sys.exit()

num1 = int(var[0])
op = var[1]
num2 = int(var[2])

res = 0

if op == "+":
    res = num1 + num2
elif op == "-":
    res = num1 - num2
elif op == "*":
    res = num1 * num2
elif op == "/":
    if num2 == 0:
        print("div by zero.")
        sys.exit()
    else:
        res = num1 / num2
else:
    print("unkown op.")
    sys.exit()
print("{:d} {:s} {:d} = {:.2f}".format(num1,op,num2,res))
