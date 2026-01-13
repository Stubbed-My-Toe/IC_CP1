#IC 1st Finance Calculator

#Saving calculator: 
def savings_calculator():
    #savings goal = int(What is your savings goal?)
    savings_goal = int(input("What is your savings goal?\n"))
    #how_often = How often do you want to deposit?
    how_often = int(input("How often do you want to deposit?\n1. Weekly\n2. Monthly\n"))
    def WorM():
        if how_often == 1:
            timeframe = "Weeks"
        elif how_often == 2:
            timeframe = "Months"
        else:
            timeframe == "However often you are depositing"
        return timeframe
    timeframe = WorM()
    #Deposit = Int(How much do you deposit to savings each time??)
    deposit = int(input("How much do you deposit each time?\n"))
    #How long it takes to save = savings goal/deposit
    how_long = savings_goal/deposit
    final_statement = print(f"It will take {how_long} {timeframe} to save up")
    return final_statement
#return (f"{how long it takes to save} months


#compound interest calculator
def compound_interest():
    #Balance = What is your preexisting balance
    balance = int(input("What is your pre-existing balance\n"))
    #time in years = How many years do you want to save?
    time_in_years = int(input("How many years do you want to save\n"))
    #Interest rate = What is your interest rate?
    interest_rate = float(input("What is the interest rate? (Enter with no percentage sign. ie: instead of 5%, use 5. and, use a point in front of the numbers, if interest is 50%, use 1.5)\n"))
    #For years in time in years:
    answer=balance * interest_rate
    print(f"You will have {answer}")
#return

#Budget allocator
def budget_allocator():
    #What is the amount you want to use on the budget?
    income = float(input("What is your income?\n"))
    #Divide balance by 100, and then multiply by 40 for rent. Multiply 15 for food and 5 for bills. 10 for savings and 30 for transportation and ten for personal use
    rent= 40*(income/100)
    food = 15*(income/100)
    utilities = 5*(income/100)
    savings = 10*(income/100)
    transportation = 30*(income/100)
    personal = 10*(income/100)
    print(f"You will have to spend {rent} on rent, {food} on food, {utilities} on utilities, {savings} on savings, {transportation} on transportation, and {personal} on personal use.")
#return

#Sales price calculator:
def sales_price():
    #how much is the original item?
    price = int(input("What is this item's original cost?\n"))
    #discount what percent is the discount?
    coupon = int(input("How much is the discount? If the discount is 5%, just put 5 and and so on\n"))
    #Divide price by 100 and then multiply by dicount. Then subtract that number from price.
    discount = price-((price/100) * coupon)
    print(discount)
#return

#Tip calculator:
def tip_calculator():
    #Bill= what is the bill?
    bill = float(input("How much does the meal or service orginally?\n"))
    #What percent of a tip are you giving?
    tip = float(input("How much of a tip are you planning to give?\n"))
    #Divide bill by one hundred then multiply and then add to bill.
    tip_calc = bill+((bill/100)*tip)
    print(f"You will have to pay {tip_calc} dollars.")
#return

#Welcome message: "What would you like to use today?"
welcome = int(input("What calculation would you like to use?\nPlease type the number of the calculation you want to use.\n\n1. Savings Calculator\n\n2. Compound Interest Calculator\n\n3. Budget Calculator\n\n4. Sale Price Calculator\n\n5. Tip Calculator\n"))
#Show Options: Savings Calculator, Compound Interest Calculator, Budget Allocator, Sale Price Allocator, Tip Calculator

#If savings:
if welcome == 1:
    savings_calculator()

elif welcome == 2:
    compound_interest()

elif welcome == 3:
    budget_allocator()

elif welcome == 4:
    sales_price()

elif welcome == 5:
    tip_calculator()

else:
    print("Please try again later.")
    exit