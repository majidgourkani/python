print("""
(-100 , -30]    very cold
(-30 , 0)       cold
0               zero
(0 , 30)        hot
[30 , 100)      very hot""")

t = int(input("enter your number: "))

if t <= -100:
    print("not ecceptable.")
if t > -100:
    if t <= -30:
        print("very cold.")
if t > -30:
    if t < 0:
        print("cold.")
if t  == 0:
    print("zero.")
if t > 0:
    if t < 30:
        print("hot.")
if t >= 30:
    if t < 100:
        print("very hot.")
if t >= 100:
    print("not acceptable.")
