#IC 1st Finance Calculator

#Saving calculator: 
def savings_calculator():
    #savings goal = int(What is your savings goal?)
    savings_goal = int(input("what is your savings goal?\n"))
    #how_often = How often do you want to deposit?
    how_often = int(input("How often do you want to deposit?\n1. Weekly\n2. Monthly\n"))
    def WorM():
        if how_often == 1:
            timeframe = "Weeks"
        elif how_often == 2:
            timeframe = "Months"
        else:
            timeframe == "however often you are depositing"
        return timeframe
    timeframe = WorM()
    #Deposit = Int(How much do you deposit to savings each time??)
    deposit = int(input("How much do you deposit each time?\n"))
    #How long it takes to save = savings goal/deposit
    how_long = savings_goal/deposit
    final_statement = print(f"It will take {how_long} {timeframe} to save up")
    return final_statement
#return (f"{how long it takes to save} months
savings_calculator()


#compound interest calculator
    #Balance = What is your preexisting balance
    #time in years = How many years do you want to save?
    #Interest rate = What is your interest rate?
    #For years in time in years:
        #multiply balance by interest rate
#return

#Budget allocator
    #What is the amount you want to use on the budget?
    #Divide balance by 100, and then multiply by 40 for rent. Multiply 15 for food and 5 for bills. 10 for savings and 30 for transportation
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
