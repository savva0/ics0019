# -*- coding: utf-8 -*-
from math import sqrt

# A function that computes quadratic equation
# No validation is done inside
# Do your own validation!
def quadratic_equation(a, b, c):
    
    if a == 0 and b == 0:
        return None

    if a == 0:
        x = - (c / b)

        return x

    d = b * b - 4 * a * c

    if d < 0:
        return None

    elif d == 0:
        x = - b / (2 * a)

        return x

    elif d > 0:
        x1 = (- b - sqrt(d)) / (2 * a)
        x2 = (- b + sqrt(d)) / (2 * a)
        
        return {"x1": x1, "x2": x2}

    else:
        return None
