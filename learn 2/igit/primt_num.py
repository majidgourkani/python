def isPrime(n):
    if n == 1:
        print("{} is special.".format(n))
        return False
    for x in range(2,n):
        if n % x == 0:
            print("{} is not primte.".format(n))
            return False
    else:
        print("{} is a prime number.".format(n))

for m in range(1,51):
    isPrime(m)
