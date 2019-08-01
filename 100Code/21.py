file = open("test1.txt")
fread = file.read()
file.close()
print(repr(fread))

text = fread.split('\n')
print(text[:-1])

#baz o khondan az ye file