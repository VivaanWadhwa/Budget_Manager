"""
Importing the necessary libraries
"""
from datetime import date

class Expense:
    
    def __init__(self, desc, amount, date,month,year):
        self.desc = desc
        self.amount = amount
        self.date = date(year,month,date)

    #Getters
    
    def get_desc(self):
        return self.desc
    
    def get_amount(self):
        return self.amount
    
    def get_date(self):
        return self.date
    

