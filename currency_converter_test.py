import pytest
from currency_converter import CurrencyConverter


def test_general():
    a = CurrencyConverter(10)
    assert a.value == 10
    a.currency = 'RUB'
    assert a.currency == 'RUB'

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

    assert str(a) == '10 RUB'
    assert repr(b) == 'Value: 2108.36 Currency: JPY'

    a.currency = 'USD'
    assert a.value == 0.146


def test_addition():
    a = CurrencyConverter(10)
    b = CurrencyConverter(1, 'USD')

    assert type(a + b) is CurrencyConverter
    assert (a + b).value == 78.4932
    assert (a + b).currency == 'RUB'

    a.currency = 'EUR'
    assert type(a + b) is CurrencyConverter
    assert (a + b).value == 0.129 + 0.8846
    assert (a + b).currency == 'EUR'

    assert (10 + a).value == 10.129
    assert (10.5 + a).value == 10.629
    assert (a + 10).value == 10.129
    assert (a + 10.5).value == 10.629

    with pytest.raises(AttributeError):
        print(a + 'str')
    with pytest.raises(AttributeError):
        print(a + [1, 2, 3])
