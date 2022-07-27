import pytest
from highest_number_finder import HighestNumberFinder

def test_find_highest_in_empty_array():
    # arrange
    numbers = [33]
    expectedResult = 33
    cut = HighestNumberFinder()

    # act 
    result = cut.find_highest_number(numbers)
    # assert

    assert expectedResult == result