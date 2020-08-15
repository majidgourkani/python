class test:
    def __init__(self, age = 15):
        self.age = age
        print("initializing, age in {}".format(self.age))
    def univers(self):
        self.age += 1
        print("new year added: {}".format(self.age))
cl1 = test(20)
cl2 = test(30)
cl3 = test()
cl1.univers()
cl1.univers()
cl2.univers()
cl3.univers()
cl1.univers()
