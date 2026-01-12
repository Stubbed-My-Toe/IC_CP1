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
    #Divide balance by 100, and then multiply by 40 for rent. Multiply 15 for food and 5 for bills. 10 for savings and 30 for transportation
    def split_cash():
        income/=100
        rent = income*40
        food = income*15
        utility = income*5
        savings = income*10
        transportation = income*30
#return

#Sales price calculator:
    #how much is the original item?
    #discount what percent is the discount?
    #Divide price by 100 and then multiply by dicount. Then subtract that number from price.
#return

#Tip calculator:
    #Bill= what is the bill?
    #What percent of a tip are you giving?
    #Divide bill by one hundred then multiply and then add to bill.
#return

#Welcome message: "What would you like to use today?"
#Show Options: Savings Calculator, Compound Interest Calculator, Budget Allocator, Sale Price Allocator, Tip Calculator

#If savings:
    #Savings 
