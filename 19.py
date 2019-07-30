def shift_values(array, sh_num):
    if sh_num < 0:
        sh_num = abs(sh_num)
        for i in range(sh_num):
            array.append(array.pop(0))
    else:
        for i in range(sh_num):
            array.insert(0, array.pop())

values = [1,2,3,4,5,6,7,8,9]

shift_values(values, -2)
print("shifted for -2 time: ", values)

shift_values(values, 4)
print("shifted for 4 time: ", values)

shift_values(values, -3)
print("shifted for -3 time: ", values)

shift_values(values, 1)
print("shifted for 1 time: ", values)

#array values shift