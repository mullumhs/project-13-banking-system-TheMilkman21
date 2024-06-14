""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: account.py
# Description: Contains the base Account class and derived classes.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Account():
    def __init__(self, name, acc_number, balance):
        self.set_name(name) 
        self.set_acc_number(acc_number)
        self.set_balance(balance)
        
    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise ValueError("put a name")
        
    def get_acc_number(self):
        return self._acc_number
    
    def set_acc_number(self, acc_number):
        if isinstance(acc_number, (int, float)) and acc_number >= 0:
            self._acc_number = acc_number
        else:
            raise ValueError("not cool")
        
    def get_balance(self):
        return self._balance
    
    def set_balance(self, balance):
        if isinstance(balance, (int, float)) and balance >= 0:
             self._balance = balance
        else:
            raise ValueError("balance cannot be negative.")
        
    def deposit(self, deposited_amount):
        if deposited_amount > 10001:
            raise ValueError("deposit less")
        else:
            print(f"successfully deposited {deposited_amount}")
        self._balance + deposited_amount
        
        
    def withdraw(self, withdraw_amount):
        if withdraw_amount > self._balance:
            raise ValueError("you dont got that much")
        else:
            print(f"you successfully withdrew {withdraw_amount}")
            self._balance - withdraw_amount
        