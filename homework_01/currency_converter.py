class CurrencyConverter:
    available_currencies = ['RUB', 'USD', 'EUR', 'KZT', 'JPY']
    currencies_dict = {
        ('RUB', 'USD'): 0.0146,
        ('RUB', 'EUR'): 0.0129,
        ('RUB', 'KZT'): 5.5898,
        ('RUB', 'JPY'): 1.5372,
        ('USD', 'EUR'): 0.8846,
        ('USD', 'KZT'): 383.407,
        ('USD', 'JPY'): 105.418,
        ('EUR', 'KZT'): 433.464,
        ('EUR', 'JPY'): 119.181,
        ('KZT', 'JPY'): 0.275,
    }
    for key, value in list(currencies_dict.items()):
        currencies_dict[(key[1], key[0])] = round(1 / value, 4)

    def __init__(self, value, currency=None):
        self.__value = value
        self.__currency = currency

    @property
    def value(self):
        return self.__value

    @property
    def currency(self):
        if self.__currency is None:
            raise AttributeError('Currency was not given')
        return self.__currency

    @currency.setter
    def currency(self, currency):
        if self.__currency != currency:
            if currency in self.available_currencies:
                if self.__currency is not None:
                    self.__value = self.__value * self.currencies_dict[self.__currency, currency]
                self.__currency = currency
            else:
                raise ValueError('Given currency is not available')

    def __add__(self, other):
        if type(other) is CurrencyConverter:
            if self.__currency is None:
                value = self.__value + other.__value
                currency = other.__currency
            else:
                value = self.__value + self.currencies_dict[other.__currency, self.__currency] * other.__value
                currency = self.__currency
            return CurrencyConverter(value, currency)
        elif type(other) in [int, float]:
            return CurrencyConverter(self.__value + other, self.__currency)
        else:
            raise AttributeError('Only numbers or other currency can be added')

    def __radd__(self, other):
        return CurrencyConverter(self.__value + other, self.__currency)

    def __str__(self):
        return '{value} {currency}'.format(
            value=self.__value,
            currency='NotGiven' if self.__currency is None else self.__currency
        )

    def __repr__(self):
        return 'Value: {value} Currency: {currency}'.format(
            value=self.__value,
            currency='NotGiven' if self.__currency is None else self.__currency
        )
