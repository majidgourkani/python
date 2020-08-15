import datetime as dt

def add(a,b,c):
    return a+b+c

print(add(2,5,8))
#####################################################
def addj(*nums):
    total = 0
    for n in nums:
        total += n
    return total

print(addj(65,65,89,646,87,9,223,9))
print(addj(651,98,65,1))
print(addj(1,2,3,4,4,56,7,9,9,7,9,9,6,23,1,86,245,8,369,3))
#####################################################
def req_time( mes , time = dt.datetime.now() ):
    print("{:} ,time {:}".format(mes , time))
req_time("it's morning")
req_time("it's morning" , "Feb 22nd 2017 10:25:08")
