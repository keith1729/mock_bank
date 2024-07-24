# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import pytz
import time
import random


# Code taken from the love-sandwiches project 
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('the_bank')


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


accounts_worksheet = SHEET.worksheet('accounts')
# accounts_data = accounts.get_all_values()

# transactions = SHEET.worksheet('transactions')
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
    username = input('\n>> ')
    account = "AC-" + str(random.randint(1000000, 9999999))
    pin = str(random.randint(1000, 9999))
    balance = str(0)

    accounts_worksheet = SHEET.worksheet('accounts')
    accounts_worksheet.append_row([username, account, pin, balance])

    print(f'\nThank you {username} for creating an account with The Bank!')
    print(f'\nYour new account number is ({account})')
    print(f'\nYour new pin number is ({pin})\n')

    login()


def login():
    '''
    Login for an existing account holder
    '''
    print(logo)

    print('\nPlease login with username and pin...')

    print('\nPlease enter your username:')
    username_entered = input('\n>> ')

    print(username_entered)

    print('\nPlease enter your pin:')
    pin_entered = input('\n>> ')

    # print(username_entered.row)

    stored_usernames = accounts_worksheet.find(username_entered, in_column=1)
    stored_pins = accounts_worksheet.find(pin_entered, in_column=3)

    if stored_usernames and stored_pins:
        if stored_usernames.row == stored_pins.row:
            print('\nLogin successful!')
            options()  
        else:
            print('\nLogin unsuccessful. Please try again...')
            welcome() 
    else:
        print('\nInvalid username or PIN. Please try again...')
        welcome()  
    


def options():
    '''
    Give options to the logged in user 
    '''
    print(logo)
    print('Would you like to [1] Deposit, [2] Withdraw or [3] see Account Details:')
    while True:
        option = input('\n>> ')
        if option.isnumeric():
            break
        print('Enter 1 or 2 or 3')
    option = int(option)

    if option == 1:
        deposit()
    elif option == 2:
        withdraw()
    elif option == 3:
        account_details()
    else:
        print('Please choose options [1], [2] or [3]')
        options()


def deposit():
    '''
    Deposits a positive value into the account
    '''
    print(logo)
    print('\nPlease enter an amount to deposit:')
    deposit_amount = int(input('\n>> '))
    
    if deposit_amount <= 0:
        print('\nYou cannot deposit a negative value or a zero value!')
        deposit()
    else:
        print('\nThank you for the deposit, updating your balance...')

        

        

def withdraw():
    print('Withdraw function')


def account_details():
    print('Account Details function')

def welcome():
    '''
    Welcome page and offers user the ability to login or create a new account
    '''

    print(logo)
    print(f'\nWould you like to [1] login or [2] create a new account? ({current_time_date()})')
    while True:
        option = input('\n>> ')
        if option.isnumeric():
            break
        print('Please enter [1] for login or [2] for create new account...')
    option = int(option)
        

    if option == 1:
        login()
    elif option == 2:
        create_new_acc()
    else:
        welcome()

welcome()
