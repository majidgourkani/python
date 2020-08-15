class fibonacchi():
    def __init__(self, a ,b):
        self.a = a
        self.b = b

    def serices(self):
        while(True):
            yield(self.b)
            self.b, self.a = self.a + self.b, self.b

f = fibonacchi(0,1)
for i in f.serices():
    if i > 100: break
    print(i, end=" ")
