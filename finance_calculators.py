import math

# Error handling
try:
    bond_or_invest = input('''Choose either 'investment' or 'bond' from the menu below to proceed:\n 
    investment - to calculate the amount of interest you'll earn on your investment 
    bond       - to calculate the amount you'll have to pay on a home loan\n\n''').lower()

    # Check if the user input is valid
    if bond_or_invest == '':
        raise ValueError("You have not made a selection!")
# If the user input is not valid, print the error message
except ValueError as err:
    print("Please enter a valid selection!")
    print("({})".format(err))

# If user inputs 'investment' as a choice then the ensuing inputs will be required from the user
if bond_or_invest == 'investment':
        amount_to_invest = float(input("\nEnter the amount you want to deposit:\n"))
        interest_rate = float(input("\nEnter the interest rate you want:\n"))
        years_to_invest = float(input("\nEnter the number of years you plan to invest for:\n"))
        interest = input("\nEnter the type of interest you want. 'Simple' or 'Compound':\n").lower()

        # Calculate the interest for both 'simple' and 'compound' based on user input
        if interest == 'simple':
            final_amount_simple = amount_to_invest * (1 + (interest_rate/100) * years_to_invest)
            print(f"\nYour investment based on simple interest will earn R {final_amount_simple}.")
        
        elif interest == 'compound':
            final_amount_compound = amount_to_invest * math.pow(1 + (interest_rate/100),years_to_invest)
            print(f"\nYour investment based on compound interest will earn R {final_amount_compound}.")

# If user inputs 'bond' as a choice then the following code will execute
if bond_or_invest == 'bond':
    property_present_value = float(input("\nEnter the present value of the house:\n"))
    interest_rate = float(input("\nEnter the interest rate for the bond:\n"))
    months_to_pay = float(input("\nEnter the number of months to repay the bond:\n"))
    
    # Calculate the repayment amount for each month.
    repayment = ((interest_rate/100) / 12) * (1/(1-(1 + (interest_rate/100)/12)**(-months_to_pay))) * property_present_value
    print(f"\nYour monthly bond repayment amount will be R {repayment}.")



