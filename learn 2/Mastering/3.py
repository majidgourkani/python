def foo():
    pass

print(foo)
bar = foo
print(bar)
foo = 5
print(foo)
print(bar.__name__)
#add attibute to function
bar.plugin_name = "demo"
print(bar.plugin_name)
print("**************************")

class test:
    class_val = 10
    def __init__(self):
        self.instance_val = 20

def my_function(self):
    print(self.class_val , self.instance_val)

#add a attribute to class in type of function
test.add = my_function

#make an object from class
c = test()
c.add()
c.class_val = 50
c.add()
c.instance_val = 80
c.add()
test.class_val = 70
c.add()
