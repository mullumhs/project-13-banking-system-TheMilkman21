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
                   
    def deposit(self, acc_number, balance, deposit_amount):    
        for acc_number in self.accounts:
            if acc_number.get_acc_number() == acc_number:
                balance + deposit_amount
                return True
            else:
                print("account does not exist")
                return False
                
    def withdraw(self, acc_number, balance, withdraw_amount):
        for acc_number in self.accounts:
            if acc_number.get_acc_number() == acc_number:
                balance - withdraw_amount
                return True        
            else:
                print("account does not exist")
                return False
        
    def transfer(self, acc_number, transfer_amount, acc1, acc2):
        for acc_number in self.accounts:
            if  acc_number.get_acc_number() == acc_number:
                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        