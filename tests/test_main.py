#! /usr/bin/python3

from src.package.main import add_numbers, sub_numbers


def test_add_numbers():
    assert add_numbers(1, 2) == 3
    assert add_numbers(-0.5, 7.3) == 6.8


def test_sub_numbers():
    assert sub_numbers(1, 2) == -1
    assert sub_numbers(7.3, -0.5) == 7.8
