str1 = input("insetr your text: ")

strs = str1.split()

print(strs)
sorted_strs = []

for i in range(len(strs)):
    for j in range(i,len(strs)):
        temp = strs[i]
        if len(temp) > len(strs[j]):
            t = strs[j]
            strs[j] = strs[i]
            strs[i] = t

print(strs)
