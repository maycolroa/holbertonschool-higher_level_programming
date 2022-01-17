#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        operation = (a / b)
    except ZeroDivisionError:
        operation = None
    finally:
        print("Inside operation: {}".format(operation))
        return operation
