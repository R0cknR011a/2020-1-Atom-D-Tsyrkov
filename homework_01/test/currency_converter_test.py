import pytest
from homework_01.currency_converter import CurrencyConverter


def test_general():
    a = CurrencyConverter(10)
    assert a.value == 10
    with pytest.raises(AttributeError):
        tmp = a.currency
    with pytest.raises(ValueError):
        a.currency = 'JPK'
    assert str(a) == '10 NotGiven'
    assert repr(a) == 'Value: 10 Currency: NotGiven'
    a.currency = 'RUB'
    assert a.currency == 'RUB'
    assert a.value == 10
    a.currency = 'USD'
    assert a.value == 0.146
    assert str(a) == '0.146 USD'
    assert repr(a) == 'Value: 0.146 Currency: USD'

    b = CurrencyConverter(20, 'USD')
    assert b.value == 20
    assert b.currency == 'USD'
    b.currency = 'JPY'
    assert b.currency == 'JPY'
    assert b.value == 2108.36

    with pytest.raises(ValueError):
        a.currency = 'JPK'
    with pytest.raises(ValueError):
        b.currency = 'USE'
    with pytest.raises(AttributeError):
        a.value = 1010
    with pytest.raises(AttributeError):
        b.value = 2020
    assert str(b) == '2108.36 JPY'
    assert repr(b) == 'Value: 2108.36 Currency: JPY'


def test_addition():
    a = CurrencyConverter(10)
    b = CurrencyConverter(1, 'USD')

    assert type(a + b) is CurrencyConverter
    assert (a + b).value == 11
    assert (a + b).currency == 'USD'
    with pytest.raises(AttributeError):
        tmp = a.currency

    a.currency = 'EUR'
    assert type(a + b) is CurrencyConverter
    assert (a + b).value == 10.8846
    assert (a + b).currency == 'EUR'

    assert (10 + a).value == 20
    assert (10.5 + a).value == 20.5
    assert (a + 10).value == 20
    assert (a + 10.5).value == 20.5

    with pytest.raises(AttributeError):
        print(a + 'str')
    with pytest.raises(AttributeError):
        print(a + [1, 2, 3])
