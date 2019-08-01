file = open("test1.txt")

lines = 0
words = 0
letters = 0

for i in file:
    lines += 1
    letters += len(i)
    words += len(i.split())
    if i[-1] == ' ' or i[-1] == ' \n':
        words -= 1

print("Lines: ", lines)
print("Words:", words)
print("Letters: ", letters)

#peyda kardan tedad anasore ye file.