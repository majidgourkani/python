alfa1 = ["a" , "d" , "e" , "b"]
alfa2 = ["f" , "h" , "g"]
alfa3 = "hjklmnopq"

alfa1.sort()
alfa2.sort()
print(alfa1)
print(alfa2)
alfa1.insert(2,"c")
print(alfa1)
print(alfa2)

strr = "".join(alfa1) + "".join(alfa2) + alfa3
print(strr)

#join a list if contain a none string type value
alfa2 = ["f" , "h" , 5 , "g"]
strr = "".join(str(x) for x in alfa2)
print(strr)
