x = int(input("insert your number: "))
y = 0

while x != 0:
    digit = x % 10
    y = y * 10 + digit
    x = x // 10

print("reverce number is: ", y)

#barax kardan argham adad