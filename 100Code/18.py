from random import randint

def search(array, ak):
    mid = len(array) // 2
    mini = 0
    maxi = len(array) - 1
    while array[mid] != ak and mini <= maxi:
        if ak > array[mid]:
            mini = mid + 1
        else:
            maxi = mid - 1
        mid = (maxi + mini) // 2
    if mini > maxi:
        return None
    else:
        return mid + 1

array_list = []
for x in range(25):
    array_list.append(randint(1,50))
array_list.sort()
print(array_list)

num = int(input("insert your number or search: "))
print(search(array_list,num))

#search yek adad dar array