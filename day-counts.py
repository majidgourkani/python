fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("File dose not exit...")
    exit()
    
counts = dict()
for line in fhand:
	if line.startswith("From"):
		try:
			day = line.split()[2]
			if day not in counts:
				counts[day] = 1
			else:
				counts[day] += 1
		except:
			continue
print(counts)
