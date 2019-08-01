num = input("insert your number: ")

while type(num) != float:
    try:
        num = float(num)
    except ValueError:
        print("your number is wrong.", end=" ")
        num = input("insert your number: ")
print(num/2)
#handle kardan khata dar vorodi
