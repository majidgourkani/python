#user input
print("please enter informatins.")
fname = str(input("enter your name: ")).title()
lname = str(input("enter your family: ")).title()
age = int(input("enter your age: "))

print("hi {name} {family}, you are {age} years old.".format(name=fname,family=lname,age=age))
