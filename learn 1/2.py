num1 = 1
num2 = 2
total = 0
next = 0
while True:
    next = num1 + num2
    if next > 4000000:
        break
    else:
        num1 = num2
        num2 = next
        if next%2 == 0:
            total += next
print(total)
