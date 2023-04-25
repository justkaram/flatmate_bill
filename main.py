from flat import Bill, Flatmate
from reports import PdfReport

# Bill Info
user_pill = float(input('Hi !, Enter the bill amount: '))
user_period = input('What is the bill period? E.g. March 2023 : ')

# Flatmate1 Info
flatmate1_name = input('Enter tha name of the first flatmate: ').title()
flatmate1_days = int(input(f'How many days did {flatmate1_name} stay at home: '))

# Flatmate2 Info
flatmate2_name = input('Enter tha name of the second flatmate: ').title()
flatmate2_days = int(input(f'How many days did {flatmate2_name} stay at home: '))

# Creating Objects
some_bill = Bill(user_pill, user_period)
flatmate_1 = Flatmate(flatmate1_name, flatmate1_days)
flatmate_2 = Flatmate(flatmate2_name, flatmate2_days)

# Print info
print(f'{flatmate_1.name} pays: {round(flatmate_1.pays(some_bill, flatmate_2), 2)}$')
print(f'{flatmate_2.name} pays: {round(flatmate_2.pays(some_bill, flatmate_1), 2)}$')

# Print pdf report for the bill
report = PdfReport('bill.pdf')
report.generate_pdf(flatmate_1, flatmate_2, some_bill)
