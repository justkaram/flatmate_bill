import webbrowser

from fpdf import FPDF

from flat import Bill, Flatmate


class PdfReport:
    """
    Generates pdf report of a bill. two flatmates have to pay
    this bill according to a certain equation.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate_pdf(self, flatmate1, flatmate2, bill):
        # Amount each flatmate has to pay
        amount_f1 = round(flatmate1.pays(bill, flatmate2), 2)
        amount_f2 = round((bill.amount - amount_f1), 2)

        # Creating a pdf obj
        pdf = FPDF(orientation='p', unit='pt', format='A4')
        pdf.add_page()

        # Setting labels
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=150, txt="Flatmates Bill", border=1, align="C", ln=1)
        pdf.set_font(family='Times', size=20, style='B')
        pdf.cell(w=100, h=40, txt="Period", border=1, align='C')
        pdf.cell(w=0, h=40, txt=f"{bill.period}", border=1, align='C', ln=1)
        pdf.set_font(family='Times', size=15, style='BI')
        pdf.cell(w=100, h=40, txt="Name", border=1, align='C')
        pdf.cell(w=150, h=40, txt="Days stayed at home", border=1, align='C')
        pdf.cell(w=0, h=40, txt="toPay", border=1, align='C', ln=1)

        # Info for the first flatmate
        pdf.set_font(family='Times', size=15)
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1, align='C')
        pdf.cell(w=150, h=40, txt=str(flatmate1.days_stayed_home), border=1, align='C')
        pdf.cell(w=0, h=40, txt=f"{amount_f1}$", border=1, align='C', ln=1)

        # Info for the Second flatmate
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=1, align='C')
        pdf.cell(w=150, h=40, txt=str(flatmate2.days_stayed_home), border=1, align='C')
        pdf.cell(w=0, h=40, txt=f"{amount_f2}$", border=1, align='C')

        pdf.output(self.filename)
        webbrowser.open(self.filename)


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
