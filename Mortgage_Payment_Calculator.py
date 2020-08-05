#### Hello this is a rough & tumble mortgage payment calulator that can give a user a general idea of how much they
#### can alter the months of a loan and it's total payment owed by changing the payment and interest fields.
from matplotlib.pyplot import plot, axis, legend, show
#### Introduction
print("Hi, I am a Py mortgage payment calculator that will help give you a better understanding of how much interest you\n"
      "can expect to pay over the life of a loan based on the amount, interest rate, and payments you plan to make!")
name = input("Let's get started! I am the Eldur, Light of Debt, may I please have your name? ")
#### User generated input fields, code to make the program hard to break
while True:
    try:
        mortgage_amount =float(input("Hi, "+name+", please enter the total amount of your loan or mortgage: "))
    except ValueError:
        print("Can you please input the amount as a number, for example 100,000 as 100000, thank you!")
        continue
    if (mortgage_amount <= 0):
        print("Mortgage amount must be positive, please enter a number again, thank you!")
    else:
        break
while True:
    try:
        interest_rate = float(input("How much is your interest rate (as a percentage) for example, please enter 3.25% as 3.25? "))/100
    except ValueError:
        print("Can you please input the amount as a number, for example 5% as 5, thank you!")
        continue
    if (interest_rate < 0):
        print("We are not calculating negative interest rates at this time, please choose 0 or higher, thank you!")
    else:
        break
while True:
    try:
        payment  = float(input("How much is your planned payment per month? "))
    except ValueError:
        print("Can you please input the amount as a number, for example 1,000 as 1000, thank you!")
        continue
    if (payment <= 0):
        print("All payments must be greater than 0, please enter a number again, thank you!")
    else:
        break
#### Store the value for the final payment calulations
beginning_principal = mortgage_amount

#### Build your lists out to store values  and a while loop to perform calulations off of the user input

#max_months = ### Can unlock to set a month limit for 10, 15, 30 year mortgage etc.
month = 0
month_list = [0]
mortgage_list = [mortgage_amount]
prinicpal_paid_list = [0]
interest_paid_list = [0]

while (mortgage_amount > 0.0): #and (month < max_months):## unlock with code above to place the calculation within a time limit!
    month += 1
    month_list.append(month)
    #determine new interest
    interest = mortgage_amount * (interest_rate/12)
    interest_paid_list.append(interest + interest_paid_list[month-1])
    #determine principal paid and remaining
    prinicpal = payment - interest
    mortgage_amount -= prinicpal
    mortgage_list.append(mortgage_amount)
    prinicpal_paid_list.append(prinicpal+prinicpal_paid_list[month-1])

#### Print out the results for the user and a graph to help them visualize the information.

total_payments = (beginning_principal) + (interest_paid_list[-1])
print(name+", here are the results!")
print("The total life of the loan/mortgage is estimated to be",month,"months.")
#print(beginning_principal)
print("The total amount of interest you can expect to pay is $",round(interest_paid_list[-1])," which is about $",round((interest_paid_list[-1])/month,2)," per month in interest.",sep="")
print("Which would bring your total payments to $",round(total_payments),".",sep="")
print(name+", we encourage you to restart the program again and change the fields, particulary by lowering the interest\n"
           "rate or increasing the amount of payments, so you can see how this impacts your total payments and the actual\n"
           "life of the loan. We hope this has been an illuminating experience for you. Until next time, farewell, " +name+"!")


plot(month_list, mortgage_list, label = "Remaining Mortgage", color = "red")
plot(month_list, prinicpal_paid_list, label ="Principal Paid", color = "blue")
plot(month_list, interest_paid_list, label="Interest Paid", color = "green")

axis([0,month,0,max(interest_paid_list[month], mortgage_list[0])])

legend()

show()


