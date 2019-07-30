x = abs(int(input("insert a number: ")))

sum = 0
mul = 1

while x != 0:
    sum += x % 10
    mul *= x % 10
    x //= 10

print("sum is: " + str(sum))
print("mult is: " + str(mul))

#majmoe argham adad