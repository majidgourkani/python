import pkgutil as pkg

data = open('note.txt','r')
lines = data.readlines()
for x in lines:
    x = x.replace('\n','')
    print(x)
