from datetime import datetime

class Transaction(object):
    UNDEFINED_DATE = datetime(1, 1, 1)
    def __init__(self, date=UNDEFINED_DATE, description='', withdrawl=0.0, deposit=0.0, balance=0.0):
        self.date = date
        self.description = description
        self.withdrawl = withdrawl
        self.deposit = deposit
        self.balance = balance

    def __str__(self):
        return '''{date} {description}'''.format(**self.__dict__)
