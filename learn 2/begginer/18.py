#diviable
num1 , num2 = int(input("num1 = ")) , int(input("num2 = "))
if (num1 % num2 == 0) or (num2 % num1 == 0):
    print("diviable")
else:
    print("not diviable")

# ignore vidie by zero
num1 , num2 = int(input("num1 = ")) , int(input("num2 = "))
if (not (num2 == 0)): # (if num2 is not 0: ) or (if num2 != 0: )
    print("result is: {:.4f}".format(num1/num2))
else:
    print("num2 is zero, divide by zero error!")

#equal names
name1 = str(input("name1: "))
name2 = str(input("name2: "))
name3 = str(input("name3: "))

if name1.lower() == name2.lower() == name3.lower():
    print("all is equal.")
else:
    print("Error!")
