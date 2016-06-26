"""5. **Next Prime Number** - Have the program find prime numbers until the user chooses to stop asking for the next one.
"""

def CheckPrime(y):
    #y is the number being check for Prime
    assert type(y) == int
    n = 2 #begining Prime guess
    Less = [] #create a list of numbers that are less than the number being check for prime
    while n < y:
        Less.append(n)
        n = n+1
    NumberOfPrimes = 0
    for i in Less:
        if y%i == 0:
            NumberOfPrimes += 1
        else:
            continue
    if NumberOfPrimes < 1:
        return("Prime")
    else:
        return("Not Prime")

def PrintPrimes():
    x=2
    y=0
    while y<1:
        if CheckPrime(x) != "Prime":
            x+=1
        elif input("Continue? y or n ") == "y" and CheckPrime(x) == "Prime":
            print (x)
            x+=1
        else:
            y+=1
            exit()

print(PrintPrimes())
