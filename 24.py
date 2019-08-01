file_name = input("please insert file name: ")

try:
    file = open(file_name)
except FileNotFoundError:
    print("File name dose not exist...")
#print(file.read())
else:
    print(file.read())
# gereftane ye file name.