import sys
def pri(a, b, c):
    print(a, b, c)

pri(1, 2, 3)
val = [1, 2, 3]
pri(*val)
val_1 = [1, 2]
val_2 = [3]
pri(*val_1, *val_2)
pri(*val_2, *val_1)

combin_val = [*val_1, *val_2]
print(combin_val)

#find package path
print(sys.path)
