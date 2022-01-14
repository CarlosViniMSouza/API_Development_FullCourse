import pytest
from code.calculations import add, sub, mult, div, BankAccount, InsuficcientFunds


@pytest.fixture
def zero_back_account():
    print("Creating a Empty Bank Account!")
    return BankAccount


@pytest.fixture
def bank_account():
    return BankAccount(25)


@pytest.mark.parametrize("num1, num2, expected",[
    (3, 4, 7),
    (8, 1, 5),
    (10, 14, 11)
])
def test_add(num1, num2, expected):
    print("Testing Funtion ADD()")
    assert add(num1, num2) == expected


def test_sub():
    assert sub(6, 2) == 4


def test_mult():
    assert mult(5, 5) == 25


def test_div():
    assert div(10, 2) == 5


def test_bank_set_initial_amount(bank_account):
    assert bank_account.balance == 50


def test_bank_default_amount(zero_bank_account):
    print("Testing my Bank Account!")
    assert zero_bank_account.balance == 0


def test_withdraw(bank_account):
    bank_account.withdraw(20)
    assert bank_account.balance == 30


def test_deposit(bank_account):
    bank_account.deposit(30)
    assert bank_account.balance == 80


def test_collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance, 6) == 55


@pytest.mark.parametrize("deposited, withdrew, expected", [
    (250, 110, 190),
    (60, 80, 10),
    (1000, 1400, 1300)
])
def test_bank_transaction(zero_back_account, deposited, withdrew, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected


def test_insufficient_funds(bank_account):
    with pytest.raises(InsuficcientFunds):
        bank_account.withdraw(500)
