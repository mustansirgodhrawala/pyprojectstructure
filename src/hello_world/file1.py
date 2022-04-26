#!/usr/bin/python3
# Hi, Mustansir here, this first file contains some simple functions and their corresponding tests are stored in
# tests_filename.py in the tests directory. I hope you
# understand how these functions are testing with pytest and how we reached a 100% code coverage in this script.


def print_hello():
    print("Hello, World!")


def custom_print(name):
    print(f"Hello, {name}!")


def name_length(name: str) -> int:
    return len(name)
