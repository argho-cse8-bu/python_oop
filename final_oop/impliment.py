class T_User:
    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password

""" User

/Can create an account.
/Can deposit and withdrawal amount. 
/Can check available balance.
/Can transfer the amount from his account to another user account.
/Can check transaction history.
/Can take a loan from the bank twice of his total amount.. """


class User(T_User):
    def __init__(self, email, password, wallet = 0) -> None:
        self.wallet = wallet
        self.T_History = []
        super().__init__(email, password)
    
    def deposit_money(self, money):
        self.wallet += money
        self.T_History.append(f'deposited: {money}')
    
    def withdraw_money(self, money):
        if money <= self.wallet:
            self.wallet -= money
            self.T_History.append(f'Withdrawed: {money}')
        else:
            print('You dont have enough money to withdraw')

    def check_wallet(self):
        return self.wallet
    
    def transfer_money(self,R_email, money):
        if money <= self.wallet:
            self.wallet -= money
            R_email.wallet += money
            #TODO: tranjection_history check......
            self.T_History.append(f"Transferred: {money} to {R_email}")
            R_email.T_History.append(f"Received: {money} from {self.email}")
        else:
            print('You dont have enough money to transfer')
        
    def transaction_history(self):
        return self.T_History
    
    def take_loan(self, bank):
        if bank.on_loan_feature:
            loan_amount = self.wallet * 2
            self.wallet += loan_amount
            self.T_History.append(f"Took a loan: {loan_amount}")
            bank.withdraw_from_bank(loan_amount)
            bank.total_loan_amount += loan_amount
        else:
            print("The bank is bankrupt")
    
""" Admin 

/Can create an account
/Can check the total available balance of the bank.
/Can check the total loan amount.
/Can on or off the loan feature of the bank.
 """
class Admin(T_User):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.bank_balance = 0
        self.total_loan_amount = 0
        self.on_loan_feature = True

    def check_bank_balance(self):
        return self.bank_balance

    def check_total_loan_amount(self):
        return self.total_loan_amount

    def on_loan_feature(self):
        self.on_loan_feature = True
        print('Loan feature on you can take loan')

    def off_loan_feature(self):
        self.on_loan_feature = False
        print('Loan feature off now for bankrupt')

    def deposit_to_bank(self, money):
        self.bank_balance += money

    def withdraw_from_bank(self, money):
        if money <= self.bank_balance:
            self.bank_balance -= money
        else:
            print('The bank is bankrupt')

    def loan_amount(self, user_email):
        if self.loan_feature_enabled:
            loan = user_email.check_wallet() * 2
            user_email.wallet += loan
            self.bank_balance -= loan
            self.total_loan_amount += loan
            user_email.T_History.append(f'Loan taken: {loan}')
        else:
            print('The bank is bankrupt')

    
