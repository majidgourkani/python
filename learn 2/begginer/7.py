#print Formating
int = 123
float = 12.3456789
sting = "string"

#{:x} and x is:
#e --> exponents
#b --> binary (base 2)
#o --> octal (base 8)
#d --> decimal (base 10)
#x --> hexadecimal (base 16)
#f --> float
#s --> string
print("my number is {:o}".format(int))

#print float format, {:.3f} --> print only 3 digit float number
print("my float number is {:.3f}".format(float))

#print with known padding {:15d} --> digit must take 15 placeself.
#{:x15d} --> digit take 15 palce, if is less than 15 character, add x befor digit
print("new number format is: {:015d}".format(int))
print("new float number format is: {:011.3f}".format(float))

#multiple print with formating
print("{1} {2} {0}".format(int,float,sting))
print("i'm {name:s}, and i'm {age:d}, and live in {city:s}".format(
    name="majid",
    age=26,
    city="tehran"
))
