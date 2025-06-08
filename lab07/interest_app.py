import locale 
import interest

locale.setlocale(locale.LC_ALL, 'en_US')

print("Weclome to the interest app!")
print("Type 'exit' to exit the program.")

def investment_app_run():
    while True:
        command = input("Would you like to calculate your final balance or the number of years it will take to reach your goal? Enter 'final balance', 'years' or 'exit':  ").strip().lower()
        if command == 'final balance':
            final_balance = interest.investment_value(
                start = float(input("What is your starting value?")), 
                interest_rate= float(input("What is the interest rate?")),
                tax_rate= float(input("What is the tax rate?")),
                deposit = int(input("How much will you deposit yearly?")),
                years = int(input("How many years will the account acquire interest?"))
            )
            print(locale.currency(final_balance, grouping = True))
        elif command == 'years': 
            years = interest.years_to_reach_goal(
                start= float(input("What is your starting value?")),
                interest_rate= float(input("What is the interest rate?")), 
                tax_rate= float(input("What is the tax rate?")), 
                deposit= int(input("How much will you deposit yearly?")),
                goal = int(input("What is your investment goal?"))
            )
            print(years, "years")
        elif command == 'exit':
            print("See you next time!")
            break
        else:
            print("Sorry I didn't get that.")

investment_app_run()