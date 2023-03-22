import pytest

from Calculator import calculator

@pytest.mark.Addition
def test_add_single_digits():
    result = calculator().add_two_num(2,3)
    assert result == 5, "The sum of 2+3 should be 5."

@pytest.mark.Addition
def test_add_double_digits():
    result = calculator().add_two_num(20,30)
    assert result == 50, "The sum of 20+30 should be 50."

@pytest.mark.Multiplication
def test_multiply_single_digits():
    result = calculator().multiply_two_num(2, 3)
    assert result == 6, "The sum of 2*3 should be 6."

@pytest.mark.Multiplication
def test_multiply_double_digits():
    result = calculator().multiply_two_num(20, 30)
    assert result == 600, "The multiplication of 20*30 should be 600."
