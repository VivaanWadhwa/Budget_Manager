"""
Importing all the necessary libraries
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector as mysql


class BudgetManager:
    income = 0
    expenses = 0
    savings = 0

    def __init__(self, income, expenses, savings):
        self.income = income
        self.expenses = expenses
        self.savings = savings
    
    #Adders

    def add_income(self,income):
        self.income += income

    def add_expenses(self,expenses):
        self.expenses += expenses

    def add_savings(self,savings):
        self.savings += savings
    
    #Getters
    def get_income(self):
        return self.income
    
    def get_expenses(self):
        return self.expenses
    
    def get_savings(self):
        return self.savings
    
    #METHODS