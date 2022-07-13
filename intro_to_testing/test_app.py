from app import a
import pytest


def test_a(mocker):
    actual = a()

    assert (actual == 99)

    mocker.patch('app.b', return_value=-1)
