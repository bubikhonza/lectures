import random

class CurrencyConverter:
    def __init__(self, curr_service):
        self.__curr_service = curr_service

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        new_rate = self.__curr_service.get_exchange_rate(from_currency, to_currency)
        result = amount * new_rate
        return result

class CurrencyService:
    def get_exchange_rate(self, from_currency: str, to_currency: str) -> float:
        return random.uniform(1.0, 1.1)
