import re 

fname = input("Enter file name: ")
try:
   fhand = open(fname)
except:
   print("File dose not exit...")
   exit()

for line in fhand: 
   line = line.rstrip() 
   x = re.findall('([0-9]+\.[0-9]+\.[0-9]+\.[0-9]{3})', line) 
   if len(x) > 0: 
      print(x) 