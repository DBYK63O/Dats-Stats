#Get Information from the User
print("Hello I am a basic savings planner and can help you determine how much you need to save for a certain goal")

name = input("My name is Tay Savings, what's your name? ")
item = input("Nice to meet you " +name+ " what would you like to save for? ")
while True:
    try:
        cost = float(input("Ok, "+name+", please enter the cost of the "+item+": "))
    except ValueError:
        print("Sorry, input must be a numerical value, please enter a valid number")
        continue
    if (cost <= 0):
        print("It doesn't look like you need to save for this item.")
        exit()
    else:
        break
while True:
    try:
       saved = float(input(name+", if you currently have any savings please enter the amount here: "))
    except ValueError:
        print("Sorry, for calculation purposes can you please input a numerical value")
        continue
    else:
        break

balance = cost - saved

period = input("Hi, " + name + ", how often will you be able to save? Please select from: (day, week, month): ")
while period not in {"day", "week", "month"}:
        period = input(("Please select either 'day', 'week', or 'month', thank you: "))

if (balance <= 0):
    print("It looks like you have enough saved at this time.")
    balance = 0
    payment = 1
while True:
    try:
        payment = float(input("Enter how much you will save each " +period+": "))
    except ValueError:
        print("Sorry, input must be a numerical value, please enter a valid number")
        continue
    if (payment <= 0):
        payment = float(input("Savings must be positive! Please enter a non-zero positive value: "))
    else:
        break

#print("Balance is", balance, "and payment is", payment)

#Calculate number of payments

num_remaining_payments = (round(balance/payment, 2))

#Present information to the User

print(name+", if you save", payment, "each "+period+", then after",num_remaining_payments,"more "+period+"s you'll have your "+item+"!")

