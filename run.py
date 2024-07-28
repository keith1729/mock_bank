# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# def options():

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

import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import pytz
import time
import random
import sys
from colorama import Fore

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

def current_time_date():
    local_tz = pytz.timezone('Europe/Dublin')
    current_tz = datetime.now(local_tz).strftime('(%H:%M:%S, %d-%m-%Y)')
    return current_tz

def characters(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.015)

class BankAccount:

    def __init__(self, username, account_number, pin, balance):
        self.username = username
        self.account_number = account_number
        self.pin = pin
        self.balance = float(balance)
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            raise ValueError('Deposit amount cannot be a negative or zero value!')

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            raise ValueError('Withdrawal amount cannot be a negative value or above your balance!')

def create_new_acc():

    time.sleep(2)
    print(f'''{Fore.YELLOW}{logo}''')
    time.sleep(2)
    characters(f'''{Fore.WHITE}
    To create a new account please enter a Username:
    ''')

    username = input('\n>> ')

    time.sleep(3)
    characters(f'''
    Generating new Account Number and new Pin for {username}...
    ''')

    account_number = 'AC-' + str(random.randint(1000000, 9999999))
    pin = str(random.randint(1000, 9999))

    balance = 0

    user_account = BankAccount(username = username, account_number = account_number, pin = pin, balance = balance)
    time.sleep(6)
    characters(f'''
    Username: {user_account.username}
    Account Number: {user_account.account_number}
    Pin: {user_account.pin}
    Balance: {user_account.balance}
    ''')

    accounts_worksheet = SHEET.worksheet('accounts')
    accounts_worksheet.append_row([user_account.username, user_account.account_number, user_account.pin, user_account.balance])

    proceed(user_account)
    time.sleep(8)
    login()

def login():

    time.sleep(2)
    print(f'''{Fore.YELLOW}{logo}''')
    time.sleep(2)
    characters(f'''{Fore.WHITE}\nPlease login with Username and Pin!\n''')

    username_entered = input('\nEnter Username: ')
    time.sleep(1)
    pin_entered = input('\nEnter Pin: ')

    try:
        # Find the row where the username matches
        username_entered_cell = accounts_worksheet.find(username_entered)
        username_entered_row = username_entered_cell.row

        # Get the data from the same row
        username_entered_row_username = accounts_worksheet.cell(username_entered_row, 1).value
        username_entered_row_account_number = accounts_worksheet.cell(username_entered_row, 2).value
        username_entered_row_pin = accounts_worksheet.cell(username_entered_row, 3).value
        username_entered_row_balance = accounts_worksheet.cell(username_entered_row, 4).value

        time.sleep(1)
        characters('\nValidating Username and Pin...\n')

        if username_entered == username_entered_row_username and pin_entered == username_entered_row_pin:
            user_account = BankAccount(username = username_entered_row_username, account_number = username_entered_row_account_number, pin = username_entered_row_pin, balance = username_entered_row_balance)
            time.sleep(6)
            print('\nLogin Successful!')
            time.sleep(6)           
        else:
            print('Cannot login! Try again...')
    except:
        print(f'Not found!')

    options(user_account)

def options(user_account):

    time.sleep(2)
    print(f'''{Fore.YELLOW}{logo}''')
    time.sleep(2)
    characters(f'''{Fore.WHITE}
    Welcome {user_account.username}!
        
    Please choose one of the following options:

    [1] Deposit
    [2] Withdraw
    [3] Show Account Details
    [4] Exit
    ''')

    option = int(input('\n>> '))

    if option == 1:
        time.sleep(2)
        print(f'''{Fore.YELLOW}{logo}''')
        time.sleep(2)
        characters(f'''{Fore.WHITE}\nTo deposit into {user_account.username}'s account
        ''')
        deposit_amount = float(input('\nEnter your deposit amount: €'))
        user_account.deposit(deposit_amount)
        time.sleep(3)
        print('\nDeposit Successful!')
        time.sleep(2)
        print(f'\nNew Balance: €{user_account.balance}\n')
        cell = accounts_worksheet.find(user_account.username)
        accounts_worksheet.update_cell(cell.row, 4, user_account.balance)
        proceed(user_account)
    elif option == 2:
        time.sleep(2)
        withdraw_amount = float(input('\nEnter your withdraw amount: €'))
        user_account.withdraw(withdraw_amount)
        time.sleep(3)
        print(f'\nWithdrawal Successful!')
        time.sleep(2)
        print(f'\nNew Balance: €{user_account.balance}\n')
        cell = accounts_worksheet.find(user_account.username)
        accounts_worksheet.update_cell(cell.row, 4, user_account.balance)
        proceed(user_account)
    elif option == 3:
        time.sleep(2)
        characters(f'''
    {user_account.username} your Account Details are as follows:
        
    Username: {user_account.username}
    Account Number: {user_account.account_number}
    Pin: {user_account.pin}
    Current Balance: €{user_account.balance}
        ''')
        time.sleep(2)
        proceed(user_account)
    elif option == 4:
        time.sleep(2)
        welcome()
    else:
        raise ValueError('Please enter a number [1-4]')

def proceed(user_account):

    characters('''
    Would you like to continue?

    Please choose one of the following options:

    [1] Continue
    [2] Exit
    ''')
    
    option = int(input('\n>> '))

    if option == 1:
        options(user_account)
    elif option ==2:
        welcome()

def welcome():

    characters(f'''{Fore.YELLOW}
 /$$$$$$$$ /$$                       /$$$$$$$                      /$$      
|__  $$__/| $$                      | $$__  $$                    | $$      
   | $$   | $$$$$$$   /$$$$$$       | $$  \\ $$  /$$$$$$  /$$$$$$$ | $$   /$$
   | $$   | $$__  $$ /$$__  $$      | $$$$$$$  |____  $$| $$__  $$| $$  /$$/
   | $$   | $$  \\ $$| $$$$$$$$      | $$__  $$  /$$$$$$$| $$  \\ $$| $$$$$$/ 
   | $$   | $$  | $$| $$_____/      | $$  \\ $$ /$$__  $$| $$  | $$| $$_  $$ 
   | $$   | $$  | $$|  $$$$$$$      | $$$$$$$/|  $$$$$$$| $$  | $$| $$ \\  $$
   |__/   |__/  |__/ \\_______/      |_______/  \\_______/|__/  |__/|__/  \\__/
''')
    
    time.sleep(2)
    print(f'{Fore.WHITE}\nWelcome to The Bank! {current_time_date()}')
    time.sleep(3)
    characters(f'''
    Please choose an option:

    [1] Login
    [2] Create New Account
    ''')
    
    login_option = int(input('\n>> '))
    
    if login_option == 1:
        login()
    elif login_option == 2:
        create_new_acc()
    else:
        raise ValueError('Please choose option [1] Login or [2] Create New Account')
        welcome()

welcome()

