
class Atm:

    def __init__(self):
        print('Welcome to ATM')
        self.balance = 0
        self.pin = '0000'
        self.menu()
    
    def menu(self):
        print('''
        1. Check Balance
        2. Withdraw
        3. Deposit
        4. Change Pin
        5. Exit
        ''')
        choice = input('Please select an option: ')
        if choice == '1':
            self.check_balance()
        elif choice == '2':
            self.withdraw()
        elif choice == '3':
            self.deposit()
        elif choice == '4':
            self.change_pin()
        elif choice == '5':
            self.exit()
        else:
            print('Invalid option')
    
    def check_balance(self):
        print(f'Your current balance is {self.balance}')
        self.menu()

    def withdraw(self):
        amount = int(input('How much would you like to withdraw? '))
        if amount > self.balance:
            print(f'Insufficient funds your current balance is {self.balance}')
        else:
            self.balance -= amount
            print(f'You have withdrawn {amount} and your new balance is {self.balance}')
        self.menu()

    def deposit(self):
        amount = int(input('How much would you like to deposit? '))
        self.balance += amount
        print(f'You have deposited {amount} and your new balance is {self.balance}')
        self.menu()

    def change_pin(self):
        new_pin = input('Please enter your new pin: ')
        if len(new_pin) == 4 and new_pin.isdigit():
            self.pin = new_pin
            print(f'Your new pin is {self.pin}')
        else:
            print('Invalid pin')
        self.menu()

    def exit(self):
        print('Thank you for banking with us')
        exit()
