str1 = input("please insert your text: ")

nums = []
x = 0

while x < len(str1):
    temp = ""
    while '0' <= str1[x] <= '9':
        temp += str1[x]
        x += 1
        if x < len(str1):
            continue
        else:
            break
    x += 1
    if temp != "":
        nums.append(int(temp))

print(nums)