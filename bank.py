""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: bank.py
# Description: Contains the facade class for the banking system.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from account import Account


class Bank_Manager():
    def __init__(self):
        self.accounts = []
        
    def add_acount(self, name, acc_number, balance):
        for existing_acc in self.accounts:
            if existing_acc.get_name() == name:
                print("already there an account") 
                return False
        account = Account(name, acc_number, balance)
        self.accounts.append(account)
        return True
                   
    def deposit(self, acc_number, deposit_amount):    
        for account in self.accounts:
            if account.get_acc_number() == acc_number:
                account.deposit(deposit_amount)
                return True
            else:
                raise ValueError("account does not exist")
                
                
    def withdraw(self, acc_number,  withdraw_amount):
        for account in self.accounts:
            if account.get_acc_number() == acc_number:
                account.withdraw(withdraw_amount)
                return True        
            else:
                raise ValueError("account does not exist")
                
        
    def transfer(self, source_acc_number, transfer_amount, dest_acc_number):
        for acc_number in self.accounts:
            if source_acc_number.get_acc_number() == acc_number:
                source_acc_number.withdraw(transfer_amount)
            else:
                raise ValueError("account not real")
             
        for acc_number in self.accounts:
            if dest_acc_number.get_acc_number() == acc_number:
                dest_acc_number.deposit(transfer_amount)
            else:
                raise ValueError("account not real")







