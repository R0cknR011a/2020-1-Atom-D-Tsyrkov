import pytest
from homework_02.median import Median


def test_general():
    median_finder = Median()
    init_array = [5, 15, 10, 20, 3]
    result = []
    for x in init_array:
        median_finder.add_num(x)
        result.append(median_finder.find_median())
    assert result == [5, 10, 10, 12.5, 10]


def test_big():
    median_finder = Median()
    init_array = [78, 69, 49, 90, 48, 40, 38, 68, 73, 35, 35, 84, 19, 22, 87, 71, 57, 23, 55, 1]
    result = []
    for x in init_array:
        median_finder.add_num(x)
        result.append(median_finder.find_median())
    assert result == [78, 73.5, 69, 73.5, 69, 59.0, 49, 58.5, 68, 58.5, 49, 58.5, 49, 48.5, 49, 58.5, 57, 53.0, 55, 52.0]
