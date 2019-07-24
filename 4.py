while True:
    o = input(" insert operator: ")
    if o == "0":
        break

    if o in  ("*", "/", "-", "+"):
        a = float(input("insert a: "))
        b = float(input("insert b: "))

        if o == "+":
            print("%.2f" %(a+b))
        elif o == "-":
            print("%.2f" %(a-b))
        elif o == "*":
            print("%.2f" %(a*b))
        elif o == "/":
            print("%.2f" %(a/b))
    else:
        print("bad oprand...")