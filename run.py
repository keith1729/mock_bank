# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# This code is from the love-sandwiches project 
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('bank_account')

accounts = SHEET.worksheet('accounts')
accounts_data = accounts.get_all_values()

transactions = SHEET.worksheet('transactions')
transactions_data = transactions.get_all_values()

# print(accounts_data)
# print(transactions_data)

def welcome():
    """
    Welcome message that shows the current date and time
    """
    current = datetime.now().strftime('%H:%M:%S %d-%m-%Y')
    print(f'Welcome to the Bank Account: {current}')
    print('Would you like to [1]login or [2]create a new account?')


welcome()
