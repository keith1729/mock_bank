# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import pytz
import time
import random


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


logo = '''
 /$$$$$$$$ /$$                       /$$$$$$$                      /$$      
|__  $$__/| $$                      | $$__  $$                    | $$      
   | $$   | $$$$$$$   /$$$$$$       | $$  \\ $$  /$$$$$$  /$$$$$$$ | $$   /$$
   | $$   | $$__  $$ /$$__  $$      | $$$$$$$  |____  $$| $$__  $$| $$  /$$/
   | $$   | $$  \\ $$| $$$$$$$$      | $$__  $$  /$$$$$$$| $$  \\ $$| $$$$$$/ 
   | $$   | $$  | $$| $$_____/      | $$  \\ $$ /$$__  $$| $$  | $$| $$_  $$ 
   | $$   | $$  | $$|  $$$$$$$      | $$$$$$$/|  $$$$$$$| $$  | $$| $$ \\  $$
   |__/   |__/  |__/ \\_______/      |_______/  \\_______/|__/  |__/|__/  \\__/
'''


accounts = SHEET.worksheet('accounts')
# accounts_data = accounts.get_all_values()

transactions = SHEET.worksheet('transactions')
# transactions_data = transactions.get_all_values()


def current_time_date():
    '''
    Generate the current date and time
    '''
    local_tz = pytz.timezone('Europe/Dublin')
    current_tz = datetime.now(local_tz).strftime('%H:%M:%S, %d-%m-%Y')
    return current_tz


def create_new_acc():
    '''
    Create a new account and update accounts worksheet
    '''

    print('\nPlease enter a username:')
    username = input('\n>>')
    account = "AC-" + str(random.randint(1000000, 9999999))
    pin = str(random.randint(1000, 9999))
    balance = str(0)

    accounts_worksheet = SHEET.worksheet('accounts')
    accounts_worksheet.append_row([username, account, pin, balance])

    print(f'\nThank you {username} for creating an account with The Bank!')
    print(f'\nYour new account number is ({account})')
    print(f'\nYour new pin number is ({pin})\n')


def login():
    '''
    Login for an existing account holder
    '''

    print(logo)

    print('\nPlease enter your username:')
    username_entered = input('\n>>')

    print('\nPlease enter your pin:')
    pin_entered = str(input('\n>>'))

    stored_usernames = accounts.find(username_entered, in_column=1)
    stored_pins = accounts.find(pin_entered, in_column=3)

    print(stored_usernames, stored_usernames.row)
    print(stored_pins, stored_pins.row)

    if stored_usernames.row == stored_pins.row:
        print('login in')


def welcome():
    '''
    Welcome page and offers user the ability to login or create a new account
    '''

    print(logo)
    print(f'\nWould you like to [1] login or [2] create a new account? ({current_time_date()})')
    while True:
        option = input('\n>>')
        if option.isnumeric():
            break
        print('Enter 1 or 2')
    option = int(option)
        

    if option == 1:
        login()
    elif option == 2:
        create_new_acc()
    else:
        welcome()

welcome()
