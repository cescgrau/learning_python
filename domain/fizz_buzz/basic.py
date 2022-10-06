from domain.fizz_buzz.tools import is_multiple_of


def map_basic(a_number):
    accumulated_result = ""
    if is_multiple_of(multiple=3, a_number=a_number):
        accumulated_result += "fizz"
    if is_multiple_of(multiple=5, a_number=a_number):
        accumulated_result += "buzz"
    if accumulated_result == "":
        accumulated_result = str(a_number)

    return accumulated_result
