"""
Fibonacci Sequence-
Enter a number and have the program generate the
Fibonacci sequence to that number or to the Nth number.
"""

def Fibonacci(num):
    try:
        val = int(num)
    except ValueError:
        print("That's not an int!")
    x=1
    y=2
    times=1
    while times <= num:
        #if x is larger, add x+y and make new variable y, vice versa. Iterate the time
        if x<y:
            #print(str(x),"+",str(y)) Check to make sure it is adding correct numbers
            x=x+y
            times+=1
        elif y<x:
            #print(str(x),"+",str(y))
            y=x+y
            times+=1
    if x>y:
        return(x)
    if y>x:
        return(y)

print(Fibonacci(50))



