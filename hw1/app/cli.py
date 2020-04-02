#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import exit
from quadratic_equation import quadratic_equation

def main():
    print("This small program now will compute a quadratic equation\n")

    print("Please provide values of a, b and c")

    print("a: ", end="")
    a = input()

    if not a.isdigit():
        print("Not a number! Exiting...")
        exit(1)

    print("b: ", end="")
    b = input()

    if not b.isdigit():
        print("Not a number! Exiting...")
        exit(1)

    print("c: ", end="")
    c = input()

    if not c.isdigit():
        print("Not a number! Exiting...")
        exit(1)

    answer = quadratic_equation(int(a), int(b), int(c))

    if not answer:
        print("No solution, sorry")

    elif isinstance(answer, dict):
        print("x1 = " + str(answer["x1"]))
        print("x2 = " + str(answer["x2"]))

    else:
        print("x = " + str(answer))

if __name__ == "__main__":
    main()