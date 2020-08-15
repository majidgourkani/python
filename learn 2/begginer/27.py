########################################
#count number of vowles character in string
def count_vowels(s , index = 0):
    if (len(s) == index): return 0

    c = s[index]
    if c in 'aeiou':
        return count_vowels(s , index + 1) + 1
    return count_vowels(s , index + 1) + 0

#########################################
#return sum of numbers
def sum(digit):
    if digit == 0: return 0
    return sum(int(digit / 10)) + digit % 10
    #return sum(digit//10) + digit % 10

#########################################
#calculate fibunachi seris
def fibo(n):
    if (n == 0) or (n == 1): return 1
    return fibo(n - 1) + fibo(n - 2)

#########################################
print(count_vowels("majid"))
print(sum(2466))
print(fibo(9))
