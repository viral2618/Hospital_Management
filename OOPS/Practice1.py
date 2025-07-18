class Account:
    bank_name="HDFC"
    def __init__(self,acc_no,balance=0):
      self.acc_no=acc_no
      self.balance=balance
      
    def credit(self,credited,sender):
        self.credited=credited
        self.sender=sender
        if self.acc_no == sender:
            self.balance+=credited
            print(f'from bank {self.bank_name} your acc no {self.acc_no} amount has been credited:INR{credited}')
    def debit(self,debited,reciver):
        self.debited=debited
        self.reciver=reciver
        if self.acc_no == reciver:
            self.balance -= debited
            print(f"from bank {self.bank_name} your acc no {self.acc_no} amount has been debited:INR{debited}")
            
    def balance_printer(self):
        print(f"from {self.acc_no} your balance is INR",self.balance)
            
a1=Account(101,1000)
a1.credit(100,101)
a1.debit(500,101)
a1.balance_printer()

a2 = Account(111,10000)
a2.debit(1000,1111)
a2.credit(1,111)
a2.balance_printer()