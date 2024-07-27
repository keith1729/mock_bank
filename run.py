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


# accounts_worksheet = SHEET.worksheet('accounts')
# accounts_data = accounts.get_all_values()

# transactions = SHEET.worksheet('transactions')
# transactions_data = transactions.get_all_values()


# def current_time_date():
#     '''
#     Generate the current date and time
#     '''
#     local_tz = pytz.timezone('Europe/Dublin')
#     current_tz = datetime.now(local_tz).strftime('%H:%M:%S, %d-%m-%Y')
#     return current_tz


# def create_new_acc():
#     '''
#     Create a new account and update accounts worksheet
#     '''
#     print('\nPlease enter a username:')
#     username = input('\n>> ')
#     account = "AC-" + str(random.randint(1000000, 9999999))
#     pin = str(random.randint(1000, 9999))
#     balance = str(0)

#     accounts_worksheet = SHEET.worksheet('accounts')
#     accounts_worksheet.append_row([username, account, pin, balance])

#     print(f'\nThank you {username} for creating an account with The Bank!')
#     print(f'\nYour new account number is ({account})')
#     print(f'\nYour new pin number is ({pin})\n')

#     login()


# def login():
#     '''
#     Login for an existing account holder
#     '''
#     print(logo)

#     print('\nPlease login with username and pin...')

#     print('\nPlease enter your username:')
#     username_entered = input('\n>> ')

#     print(username_entered)

#     print('\nPlease enter your pin:')
#     pin_entered = input('\n>> ')

#     # print(username_entered.row)

#     stored_usernames = accounts_worksheet.find(username_entered, in_column=1)
#     stored_pins = accounts_worksheet.find(pin_entered, in_column=3)

#     if stored_usernames and stored_pins:
#         if stored_usernames.row == stored_pins.row:
#             print('\nLogin successful!')
#             options()  
#         else:
#             print('\nLogin unsuccessful. Please try again...')
#             welcome() 
#     else:
#         print('\nInvalid username or PIN. Please try again...')
#         welcome()  
    


# def options():
#     '''
#     Give options to the logged in user 
#     '''
#     print(logo)
#     print('Would you like to [1] Deposit, [2] Withdraw or [3] see Account Details:')
#     while True:
#         option = input('\n>> ')
#         if option.isnumeric():
#             break
#         print('Enter 1 or 2 or 3')
#     option = int(option)

#     if option == 1:
#         deposit()
#     elif option == 2:
#         withdraw()
#     elif option == 3:
#         account_details()
#     else:
#         print('Please choose options [1], [2] or [3]')
#         options()


# def deposit():
#     '''
#     Deposits a positive value into the account
#     '''
#     print(logo)
#     print('\nPlease enter an amount to deposit:')
#     deposit_amount = int(input('\n>> '))
    
#     if deposit_amount <= 0:
#         print('\nYou cannot deposit a negative value or a zero value!')
#         deposit()
#     else:
#         print('\nThank you for the deposit, updating your balance...')

        

        

# def withdraw():
#     print('Withdraw function')


# def account_details():
#     print('Account Details function')


# class BankAccount():

#     def __init__(self, username, account, pin, balance = 0):
#         self.username = username
#         self.account = account
#         self.pin = pin
#         self.balance = balance


#     def deposit(self, amount):
#         self.balance += amount


#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             print('You have insufficient funds!')


#     def generate_acc_num():
#         account_num = "AC-" + str(random.randint(1000000, 9999999))
#         return account_num


#     def generate_pin_num():
#         pin_num = str(random.randint(1000, 9999))
#         return pin_num


# accounts_worksheet = SHEET.worksheet('accounts')


# def current_time_date():
#     '''
#     Generate the current date and time
#     '''
#     local_tz = pytz.timezone('Europe/Dublin')
#     current_tz = datetime.now(local_tz).strftime('%H:%M:%S, %d-%m-%Y')
#     return current_tz


# def create_new_acc():
#     '''
#     Create a new account and update accounts worksheet
#     '''
#     print('\nPlease enter a username:')
#     username = input('\n>> ')
#     account_number = "AC-" + str(random.randint(1000000, 9999999))
#     pin = str(random.randint(1000, 9999))
#     balance = str(0)

#     accounts_worksheet = SHEET.worksheet('accounts')
#     accounts_worksheet.append_row([username, account_number, pin, balance])

#     print(f'\nThank you {username} for creating an account with The Bank!')
#     print(f'\nYour new account number is ({account_number})')
#     print(f'\nYour new pin number is ({pin})\n')

#     login()


# def login():
#     '''
#     Login for an existing account holder
#     '''
#     print(logo)

#     print('\nPlease login with username and pin...')

#     print('\nPlease enter your username:')
#     username_entered = input('\n>> ')

#     print('\nPlease enter your pin:')
#     pin_entered = input('\n>> ')

#     # print(username_entered.row)

#     stored_usernames = accounts_worksheet.find(username_entered, in_column=1)
#     stored_pins = accounts_worksheet.find(pin_entered, in_column=3)

#     if stored_usernames and stored_pins:
#         if stored_usernames.row == stored_pins.row:
#             print('\nLogin successful!')
#             options()  
#         else:
#             print('\nLogin unsuccessful. Please try again...')
#             welcome() 
#     else:
#         print('\nInvalid username or PIN. Please try again...')
#         welcome()  

    
    

# def options():
#     '''
#     Give options to the logged in user 
#     '''
#     print(logo)
#     print('Would you like to [1] Deposit, [2] Withdraw or [3] see Account Details:')
#     while True:
#         option = input('\n>> ')
#         if option.isnumeric():
#             break
#         print('Enter 1 or 2 or 3')
#     option = int(option)

#     if option == 1:
#         deposit()
#     elif option == 2:
#         withdraw()
#     elif option == 3:
#         account_details()
#     else:
#         print('Please choose options [1], [2] or [3]')
#         options()


# def deposit():
#     '''
#     Deposits a positive value into the account
#     '''
#     print(logo)
#     print('\nPlease enter an amount to deposit:')
#     deposit_amount = int(input('\n>> '))
    
#     if deposit_amount <= 0:
#         print('\nYou cannot deposit a negative value or a zero value!')
#         deposit()
#     else:
#         print('\nThank you for the deposit, updating your balance...')
    
#     # Gets the user's name from the database
#     # username = accounts_worksheet.find(username_entered, in_column=1)

#     # Gets the current balance amount in the account
#     balance = accounts_worksheet.find(username_entered.col + 3).value

#     balance += deposit_amount


# def welcome():

#     print(logo)
#     print(f'\n({current_time_date()})')
#     while True:
#         option = input('\n>> ')
#         if option.isnumeric():
#             break
#         print('Please enter [1] for login or [2] for create new account...')
#     option = int(option)
        

#     if option == 1:
#         login()
#     elif option == 2:
#         create_new_acc()
#     else:
#         welcome()

# welcome()


def current_time_date():
    local_tz = pytz.timezone('Europe/Dublin')
    current_tz = datetime.now(local_tz).strftime('%H:%M:%S, %d-%m-%Y')
    return current_tz


class BankAccount:
    def __init__(self, username, account_number, pin_number, balance):
        self.username = username
        self.account_number = account_number
        self.pin_number = pin_number
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            raise ValueError('Deposit amount cannot be a negative or zero value!')

    def withdraw(self, amount):
        if 0 > amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            raise ValueError('Withdrawal amount cannot be a negative value or above your balance!')


def welcome():

    print(logo)
    print(f'\nWelcome to The Bank! {current_time_date()}')
    print('\nPlease choose an option:')
    print('\n[1] Login')
    print('[2] Create New Account')
    login_option = int(input('\n>> '))
    if login_option == 1:
        login()
    elif login_option == 2:
        create_new_acc()
    else:
        ValueError('Please choose option [1] Login or [2] Create New Account')
        welcome()


def login():

    print('\nPlease login with Username and Pin!')
    username_entered = input('\nEnter Username: ')
    pin_entered = input('\nEnter Pin: ')

# def login():
#     '''
#     Login for an existing account holder
#     '''
#     print(logo)

#     print('\nPlease login with username and pin...')

#     print('\nPlease enter your username:')
#     username_entered = input('\n>> ')

#     print('\nPlease enter your pin:')
#     pin_entered = input('\n>> ')

#     # print(username_entered.row)

#     stored_usernames = accounts_worksheet.find(username_entered, in_column=1)
#     stored_pins = accounts_worksheet.find(pin_entered, in_column=3)

#     if stored_usernames and stored_pins:
#         if stored_usernames.row == stored_pins.row:
#             print('\nLogin successful!')
#             options()  
#         else:
#             print('\nLogin unsuccessful. Please try again...')
#             welcome() 
#     else:
#         print('\nInvalid username or PIN. Please try again...')
#         welcome()  

def create_new_acc():

    print('\nTo create a new account please enter a username:')
    username_entered = input('\n>> ')

    print('\nGenerating account number and pin...')
    account_number = 'AC-' + str(random.randint(1000000, 9999999))
    pin_number = str(random.randint(1000, 9999))

    balance = 0

    user_account = BankAccount(username = username_entered, account_number = account_number, pin_number = pin_number, balance = balance)
    print(f'\nUsername: {user_account.username}')
    print(f'\nAccount Number: {user_account.account_number}')
    print(f'\nPin Number: {user_account.pin_number}')
    print(f'\nBalance: {user_account.balance}\n')

    accounts_worksheet = SHEET.worksheet('accounts')
    accounts_worksheet.append_row([user_account.username, user_account.account_number, user_account.pin_number, user_account.balance])


    
#     print('\nPlease enter a username:')
#     username = input('\n>> ')
#     account = "AC-" + str(random.randint(1000000, 9999999))
#     pin = str(random.randint(1000, 9999))
#     balance = str(0)

#     accounts_worksheet = SHEET.worksheet('accounts')
#     accounts_worksheet.append_row([username, account, pin, balance])

#     print(f'\nThank you {username} for creating an account with The Bank!')
#     print(f'\nYour new account number is ({account})')
#     print(f'\nYour new pin number is ({pin})\n')

#     login()


welcome()