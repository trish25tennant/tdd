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

def test_find_highest_in_array_of_two_descending():
    # arrange
    numbers = [14, 7]
    expectedResult = 14
    cut = HighestNumberFinder()

    # act 
    result = cut.find_highest_number(numbers)
    # assert

    assert expectedResult == result

def test_find_highest_in_array_of_two_ascending():

    numbers =[7,14]
    expectedResult=14
    cut=HighestNumberFinder()
    result=cut.find_highest_number(numbers)
    assert expectedResult==result