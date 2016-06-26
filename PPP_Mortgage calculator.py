"""**Mortgage Calculator** - Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate. Also figure out how long it will take the user to pay back the loan. For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually)."""

def MonthlyPayment():

    #user input for each of the variables
    price = input("What is the price of the home?  ")
    interest = input("What is the interest rate?  Decimal format.")
    period = input("What is the period of the loan? Input in years.  ")

    #convert all to floats
    price = float(price)
    interest = float(interest)
    period = float(period)

    #convert the period in years to months
    period = period*12

    interest = interest+1
    payment = price/period
    payment = round(payment*interest, 2)

    return (payment)

print(MonthlyPayment())