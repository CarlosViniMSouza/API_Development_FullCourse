import pytest
from code.calculations import add, sub, mult, div, BankAccount, InsuficcientFunds


@pytest.fixture
def zero_back_account():
    print("Creating a Empty Bank Account!")
    return BankAccount


@pytest.fixture
def bank_account():
    return BankAccount(25)


@pytest.mark.parametrize("num1, num2, expected",
                         [
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

