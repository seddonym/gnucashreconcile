from datetime import date
from moneyed import Money, GBP
from .book import Transaction


class Suggestion:
    def __init__(self, transaction, debit_account=None, credit_account=None):
        self.transaction = transaction
        self.debit_account = debit_account
        self.credit_account = credit_account

    @property
    def date(self):
        return self.transaction.date

    @property
    def description(self):
        return self.transaction.description
    
    @property
    def amount(self):
        return self.transaction.amount
    

class Matcher:
    def __init__(self, config, book):
        pass

    def get_suggestions(self):
        return [
            Suggestion(
                Transaction(date(2017, 3, 19), 'CASH 19 MAR', Money(30, GBP)),
                debit_account='Assets.Current Account',
                credit_account='Expenses.Groceries',
            ),
            Suggestion(
                Transaction(date(2017, 3, 21), 'Monthly Salary', Money(1500, GBP)),
                debit_account='Income.Salary',
                credit_account='Assets.Current Account',
            ),
        ]
