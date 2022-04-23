#!/usr/bin/python3
from hello_world.hello import print_hello, custom_print


def test_main(capfd):
    print_hello()
    out, err = capfd.readouterr()
    assert out == "Hello, World!\n"


def test_custom_main(capfd):
    custom_print("Tom")
    out, err = capfd.readouterr()
    assert out == "Hello, Tom!\n"
