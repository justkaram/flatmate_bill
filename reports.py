from fpdf import FPDF
import webbrowser


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
