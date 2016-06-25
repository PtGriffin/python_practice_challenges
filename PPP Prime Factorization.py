"""
Prime Factorization
Have the user enter a number and find all Prime Factors (if there are any) and display them.
"""

def PrimeFactorize(num):
    assert type(num) == int
    if CheckPrime(num) == "Prime":
        return(num," is prime")

    PrimeNsLess = [] #list of all primes less than the number input
    x=2
    while x<num:
        if CheckPrime(x) == "Prime":
            PrimeNsLess.append(x)
            x+=1
        else:
            x+=1
            continue

    Factors = []
    while CheckPrime(num) != "Prime":
        for i in PrimeNsLess: #Check which primes
            remainder = num%i
            if remainder == 0:
                Factors.append(i)
                num = int(num/i)
            elif remainder != 0:
                continue
    if CheckPrime(num) == "Prime" and num != 1:
        Factors.append(num)
    return Factors



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


#print(CheckPrime(10007))
print(PrimeFactorize(105))