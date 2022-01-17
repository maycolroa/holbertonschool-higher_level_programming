#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        splitting_operation = (a / b)
    except ZeroDivisionError:
        splitting_operation = None
    finally:
        print("Inside splitting_operation: {}".format(splitting_operation))
        return splitting_operation
