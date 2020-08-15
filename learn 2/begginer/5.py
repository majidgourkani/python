str1 = "UPPERCASESENTENS"
str2 = "lowercasesentens"

print(str2.upper())
print(str2)

temp = str2.upper()
print(temp)

print(str1.lower())
print(str1.title())

str3 = "   majid                "
print(str3)
#.strip() method remove white space from first and end of string, not middle
print(str3.strip())

str4 = "    majid   was here            "
print(str4)
print(str4.strip().title())
