class employee:
    def __init__(self, firstname, lastname):
        self.fname = firstname
        self.lname = lastname
    def employee(self):
        return self.fname + ' ' + self.lname

names = []
for i in range(2):
    firstname = input("insert fisrt name: ")
    lastname = input("insert last name: ")
    names.append(employee(firstname, lastname))

for x in names:
    print(x.employee())

#insert kardan object haye ye calss va farakhonie ona