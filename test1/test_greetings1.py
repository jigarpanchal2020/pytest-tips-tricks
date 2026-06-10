import pytest

from greeting import my_name

@pytest.fixture
def name_bob():
    return "My name is: bob"


def test_my_name(name_bob):
    assert name_bob == my_name("bob")
