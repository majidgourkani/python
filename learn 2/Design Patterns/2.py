import time

def timing(some_function):
    def wrapper():
        t1 = time.time()
        time.sleep(3)
        some_function()
        t2 = time.time()
        print("it took to run function is: {:}\n".format(t2-t1))
    return wrapper
@timing
def my_function():
    my_list = []
    for i in range(1000):
        my_list.append(i)
    sumation = sum(my_list)
    print("sum of list is: {:d}".format(sumation))

#wrapper_function = timing(my_function)
#wrapper_function()
######################################################
my_function()
