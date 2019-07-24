in_num = int(input("insert your num: "))
base_num = int(input("insert your base num: "))

if base_num not in range(2,10):
    quit("bad base num...")

result_num = ""

while in_num > 0:
    result_num = str(in_num%base_num) + result_num
    in_num //= base_num

print(result_num)