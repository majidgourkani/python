#other stuff with lists
alfa = ["a" , "b" , "c" , "d"]
print(alfa)

#2 kind of appending to list
alfa.append("e")
alfa = alfa + ["f" , "g"]
print(alfa)

e_index = alfa.index("e")
print(e_index)
del alfa[e_index]
print(alfa)

alfa.remove("d")
print(alfa)
