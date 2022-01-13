def add(num1: int, num2: int):
    return num1 + num2


def sub(num1: int, num2: int):
    return num1 - num2


def mult(num1: int, num2: int):
    return num1 * num2


def div(num1: int, num2: int):
    return num1 / num2


class InsuficcientFunds(Exception):
    pass


class BankAccount():

    def __init__(self):
        self.balance = starting_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsuficcientFunds("Insufficient Funds in your account!")

        self.balance -= amount

    def collect_interest(self):
        self.balance *= 1.1
