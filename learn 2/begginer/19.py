s = "majid gourkani"
n = [1,3,5,6,8,9,0]

print( 3 in n )
print( "aji" in s )

for num in [3,4,554,6,7,7,8,9,0,0,5,3423,23,2]:
    print(num)

num = [2,43,543,54,645,76,85,4,234,24,2342,2546,7]
print(range(len(num)))
for x in num:
    print(x)

for x in range(len(num)):
    print("index: {:d} ,number is {:d}".format((x+1),num[x]))
