
from app import get_even_numbers, get_unique_items


def test_get_even_numbers():
    assert get_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_get_unique_items():
    assert sorted(get_unique_items([1, 2, 2, 3, 3, 3])) == [1, 2, 3]
