try:
    file = open("test.txt")
    for x in file.readlines:
        print(x)
except IOError as e:
    print("there is no file, Error: {}".format(e)) #IOError
