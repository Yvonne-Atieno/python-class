# Add these attributes and behaviors to the class Account
# Add attributes deposits and withdrawals in the init method
# which are empty lists by default and another attribute loan_balance
#  which is zero by default.
class Account:
    def __init__(self):
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0
# Add a method check_balance which returns the account’s balance
    def check_balance(self):
        return self.balance
# Update the deposit method to append each withdrawal transaction
# to the deposits list. Each transaction should be in form
# of a dictionary like this
# {
#    "amount": amount,
#    "narration": “deposit”
# }
    def deposit(self, amount):
        self.balance += amount
        deposit_transaction = {
            "amount": amount,
            "narration": "deposit"
        }
        self.deposits.append(deposit_transaction)
# Update the withdrawal method to append each
#  withdrawal transaction to the withdrawals list.
#  Each transaction should be in form of a dictionary like like this
# {
#    "amount": amount,
#    "narration": “withdrawal”
# }
    def withdrawal(self, amount):
        if self.balance < amount:
            return "Insufficient funds"
        else:
            self.balance -= amount
            withdrawal_transaction = {
                "amount": amount,
                "narration": "withdrawal"
            }
            self.withdrawals.append(withdrawal_transaction)
# Add a new method  print_statement which combines
# both deposits and withdrawals into one list and,
# using a for loop, prints each transaction in a new line like this
# deposit - 1000
# withdrawal - 500
    def print_statement(self):
        transactions = self.deposits + self.withdrawals
        for transaction in transactions:
            narration = transaction["narration"]
            amount = transaction["amount"]
            print(narration, "-", amount)
# Add a borrow_loan method which allows a
#  customer to borrow if they meet these conditions:
# Account has no outstanding loan
# Loan amount requested is more than 100
# Customer has made at least 10 deposits.
# Amount requested is less than or equal to 1/3
# of their total sum of all deposits.
# A successful loan increases the loan_balance by requested amount
    def borrow_loan(self, amount):
        if self.loan_balance == 0 and len(self.deposits) > 10 and amount > 100 and amount <= (1/3 * sum(self.deposits)):
            self.loan_balance += amount
            self.balance += amount
            return "Loan approved"
        else:
            return "Loan not approved"
# Add a repay_loan method with this functionality
# A customer can repay a loan to reduce the current loan_balance
# Overpayment of a loan increases the accounts current balance
    def repay_loan(self, amount):
        if amount > self.loan_balance:
            self.balance += amount - self.loan_balance
            self.loan_balance = 0
            return "Loan fully repaid"
        else:
            self.loan_balance -= amount
            self.balance += amount
            return "Loan partially repaid"
# Add a transfer method which accepts
#  two attributes (amount and instance of another account).
# If the amount is less than the current ins
# tances balance, the method transfers the requested amount from
# the current account to the passed account. The transfer is
# accomplished by reducing the current account balance
#  and depositing the requested amount to the passed account.
    def transfer(self, amount, account):
        if self.balance >= amount:
            self.balance -= amount
            account.deposit(amount)
            return "Transfer successful"
        else:
            return "Insufficient funds for transfer"
#  two attributes (amount and instance of another account).
# If the amount is less than the current ins
# tances balance, the method transfers the requested amount from
# the current account to the passed account. The transfer is
# accomplished by reducing the current account balance
#  and depositing the requested amount to the passed account.
    def transfer(self, amount, account):
        if self.balance >= amount:
            self.balance -= amount
            account.deposit(amount)
            return "Transfer successful"
        else:
            return "Insufficient funds for transfer"









