#!/usr/bin/python3
import pytest

from hello_world.file1 import custom_print
from hello_world.file1 import name_length
from hello_world.file1 import print_hello


def test_main(capfd):
    print_hello()
    out, err = capfd.readouterr()
    assert out == "Hello, World!\n"


def test_custom_main(capfd):
    custom_print("Tom")
    out, err = capfd.readouterr()
    assert out == "Hello, Tom!\n"


@pytest.mark.parametrize(
    ("name", "expected", "error"),
    (
        pytest.param("Mustansir", 9, False, id="simple_name_test"),
        pytest.param("", 0, False, id="empty_string_test"),
        pytest.param(9, None, True, id="integer_test."),
    ),
)
def test_name_length(name, expected, error):
    # name_length("Mustansir")
    # out, err = capfd.readouterr()
    if error:
        with pytest.raises(TypeError):
            name_length(name)
    else:
        assert name_length(name) == expected
