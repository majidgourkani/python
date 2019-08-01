text = []

for i in open("test1.txt"):
    if i[-1] == '\n':
        text.append(i[:-1])

print(text)

#baz kardan file ba method open()