import locale
locale.setlocale(locale.LC_ALL, 'en_US')

def investment_value(start, interest_rate, tax_rate, deposit, years):
    balance = start
    for _ in range(1, years + 1):
        interest_earned = balance * interest_rate
        taxes = interest_earned * tax_rate
        balance += (interest_earned - taxes + deposit)
    return balance

#print(investment_value(1000, 0.07, 0.13, 1000, 10))

def years_to_reach_goal(start, interest_rate, tax_rate, deposit, goal):
    years = 0
    balance = start
    while balance < goal:
        interest_earned = balance * interest_rate
        taxes = interest_earned * tax_rate
        balance += (interest_earned - taxes + deposit)
        years += 1
    return years


#for loc in ['en_US', 'ru_RU', 'fr_FR', 'de_DE', 'es_ES', 'it_IT', 'fr_CA']:
#   locale.setlocale(locale.LC_ALL, loc)
#   print(locale.currency(35888382152.22815, grouping=True))
