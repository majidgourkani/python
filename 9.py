extensions = ['txt','jpg','svg','doc','mkv','exe','mp4','mp3']

filexe = input("insert your file with extension: ").split('.')
ext = filexe[-1].lower()

if len(ext) > 2:
    if ext in extensions:
        print("right format...")
    else:
        print("wrong format...")
else:
    print("there is a wrong file!!!")