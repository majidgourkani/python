num = [1,2,3,4,5,6,7,8,9]
name = "Majid Gourkani"
val = 586

print('__iter__' in dir(num))
print('__iter__' in dir(name))
print('__iter__' in dir(val))

itrat_list = iter(num)
while True:
    print(next(itrat_list))
