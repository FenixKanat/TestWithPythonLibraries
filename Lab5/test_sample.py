import conftest
import math
import unittest

# Test case 1
def test_circumference_1():
    output = conftest.circumference_of_circle(2 / math.pi)
    assert output == 4

def test_area_1():
    output = conftest.area_of_circle(2 / math.sqrt(math.pi))
    assert output == 4

# Test case 2
def test_circumference_2():
    output = conftest.circumference_of_circle(2 / math.sqrt(math.pi))
    assert output == 7

def test_area_2():
    output = conftest.area_of_circle(2 / math.pi)
    assert output == 1

# Test case 3
def test_circumference_3():
    output = conftest.circumference_of_circle(1)
    assert output == 2 * math.pi

def test_area_3():
    output = conftest.area_of_circle(1)
    assert output == math.pi

# Test case 4
def test_circumference_4():
    output = conftest.circumference_of_circle(2 / math.pi)
    assert round(output) == 4

def test_area_4():
    output = conftest.area_of_circle(2 / math.sqrt(math.pi))
    assert round(output) == 4


if __name__ == '__main__':
    print("Fenix Kanat")
    unittest.main()