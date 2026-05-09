import random

class BankAccount:

    def __init__(self, bank = 'mono', balance=0):
        self.bank = bank
        self.account_number = random.randint(0,1000)
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"+ ${amount}")
        else:
            raise ValueError("amount cannot be negative.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"- ${amount}")
        else:
            raise ValueError("not enough money on account.")

    def show_balance(self):
        print(f'Account: {self.account_number}')
        print(f'Balance: ${self.balance}')


class Bank:

    def __init__(self, name, commission = 0):
        self.name = name
        self.commission = commission
        self.transfer_balance = 0

    def transfer(self, account_from: BankAccount, account_to: BankAccount, amount):
        sum_commission = 0

        account_from.withdraw(amount)

        if account_from.bank != account_to.bank:
            sum_commission = amount * 0.01
            self.transfer_balance += sum_commission

        account_to.deposit(amount-sum_commission)

        print(f'Transfer ✅ from {account_from.account_number} to {account_to.account_number} amount ${amount-sum_commission} was successful.')


mono_1 = BankAccount()
mono_1.deposit(1000)

mono_2 = BankAccount()

privat_1 = BankAccount(bank='privat')

monoBank = Bank('Mono')

monoBank.transfer(mono_1, privat_1,50)

mono_1.show_balance()

privat_1.show_balance()