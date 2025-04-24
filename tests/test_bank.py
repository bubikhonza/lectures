from bank_app.bank_account import BankAccount
import pytest
from unittest.mock import patch, MagicMock

from bank_app.currency import CurrencyService, CurrencyConverter

@pytest.fixture
def test_curr_service():
    mock = MagicMock(spec=CurrencyService)
    mock.get_exchange_rate.return_value = 1
    return mock

@pytest.fixture
def test_curr_converter(test_curr_service):
    return CurrencyConverter(test_curr_service)


@pytest.fixture
def bank_account_without_bonus(test_curr_converter):
    return BankAccount("Honza", 100, "CZK", test_curr_converter)

def test_bank_account_balance_without_bonus(bank_account_without_bonus):
    assert bank_account_without_bonus.get_balance() == 100


def test_bank_account_withdraw(bank_account_without_bonus):
    bank_account_without_bonus.withdraw(50, "CZK")
    assert bank_account_without_bonus.get_balance() == 50

@pytest.mark.parametrize("x, y, result", [
    (1, 1, 2),
    (5, 5, 10),
    (-5, 5, 0)
])
def test_add_numbers(x, y, result):
    assert x + y == result

