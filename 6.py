str1 = "majid, milad, hamid, saeed, vahid"
print(str1)

str2 = input("insert string: ")
str3 = input("insert replace: ")

if (str1.find(str2) >= 0):
    i = str1.find(str2)
    str1 = str1[:i] + str3 + str1[i+len(str2):]
print(str1)