import math

a = int(input("insert your number: "))

if a < 2:
    quit("bad number...")
elif a == 2:
    print("this is prinm number...")
    quit()
else:
    y = 2
    while y <= (math.sqrt(a)):
        if a%y == 0:
            print("this is complex number...")
            print(y)
            quit()
        y += 1
    else:
        print("this is a prime number...")