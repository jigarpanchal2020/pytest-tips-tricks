import pytest

class Fruit:
    def __init__(self, name):
        self.name = name
    
    def __eq__(self, other):
        return self.name == other.name

@pytest.fixture
def my_fruit():
    return Fruit("apple")

@pytest.fixture
def fruit_basket(my_fruit):
    return [my_fruit, Fruit("banana")]

def test_fruit_equality(my_fruit, fruit_basket):
    assert my_fruit in fruit_basket