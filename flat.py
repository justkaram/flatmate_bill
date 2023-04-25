class Bill:
    """
    Object that contains data about the bill, such as
    the total amount and the period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates an object of a person who lives in a flat
    and pays a share of the bill.
    """

    def __init__(self, name, days_stayed_home):
        self.name = name
        self.days_stayed_home = days_stayed_home

    def pays(self, bill, second_flatmate):
        formula = self.days_stayed_home / (self.days_stayed_home + second_flatmate.days_stayed_home)
        to_pay = bill.amount * formula
        return to_pay
