from bank_app.currency import CurrencyConverter

class BankAccount:
    def __init__(self, owner: str, balance: float, account_currency: str, curr_converter: CurrencyConverter, bonus: int = 0) -> None:
        self.__owner = owner
        self.__balance = balance + bonus
        self.__account_currency = account_currency

        self.__curr_converter = curr_converter

    def deposit(self, amount: float, currency: str) -> float:
        converted_amount = self.__curr_converter.convert(amount, currency, self.__account_currency)
        self.__balance += converted_amount
        return self.__balance

    def withdraw(self, amount: float, currency: str) -> float:
        converted_amount = self.__curr_converter.convert(amount,self.__account_currency, currency)
        self.__balance -= converted_amount
        return self.__balance

    def get_balance(self) -> float:
        return self.__balance