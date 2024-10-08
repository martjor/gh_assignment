from example_functions import my_adder, my_thermo_stat, have_digits
import pytest

@pytest.mark.parametrize("test_input,expected",[("my_adder(1,2,3)",6),("my_adder(1,1,1)",3),("my_adder(-1,-1,2)",0)])
def test_my_adder(test_input,expected):
    assert eval(test_input) == expected

@pytest.mark.parametrize("test_input,expected",[("my_thermo_stat(0,5)",'off'),("my_thermo_stat(0,10)",'Heat'),("my_thermo_stat(20,10)",'AC')])
def test_my_thermo_stat(test_input,expected):
    assert eval(test_input) == expected

@pytest.mark.parametrize("test_input,expected",[("have_digits('Birthday')",0),("have_digits('haveMay 2001')",1),("have_digits('I wake up at 6:35')",1)])
def test_have_digits(test_input,expected):
    assert eval(test_input) == expected
