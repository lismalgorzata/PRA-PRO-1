class bank_account():
    
    def __init__(self,account_nr):
        self.account_nr=account_nr
        self.balance=0
        self.is_open=False
    
    def open_acc(self):
        self.is_open=True
        print('Welcome', '\n')
    def close_acc(self):
        self.is_open=False
        print('Goodbye')
        
    def show_status(self):
        print('Bank Account No: ',self.account_nr)
        print('Balance: PLN ', self.balance, '\n')
        
    def deposit(self, money):
        self.money=money
        self.balance=self.balance+self.money
        
    def withdraw(self, money):
        self.money=money
        if self.money>self.balance:
            print("Insufficient funds on the account", '\n')
        else:
            self.balance=self.balance-self.money
            
ba=bank_account('12 3456 5555 9090 1111 0000 7722')
ba.open_acc()
ba.show_status()
ba.deposit(25.30)
ba.show_status()
ba.withdraw(31.10)
ba.show_status()
ba.withdraw(14.0)
ba.show_status()
ba.close_acc()