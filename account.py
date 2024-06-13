""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: account.py
# Description: Contains the base Account class and derived classes.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Account():
    def __init__(self, name, acc_number, balance):
        self.get_name(name) 
        self.get_acc_number(acc_number)
        self.get_balance(balance)
        
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
            raise ValueError("Price cannot be negative.")