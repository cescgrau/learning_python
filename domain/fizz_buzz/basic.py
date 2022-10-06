from domain.fizz_buzz.tools import is_multiple_of_five, is_multiple_of_three


def map_basic(a_number):
    accumulated_result = ""
    if is_multiple_of_three(a_number):
        accumulated_result += "fizz"
    if is_multiple_of_five(a_number):
        accumulated_result += "buzz"
    if not is_multiple_of_three(a_number) and not is_multiple_of_five(a_number):
        accumulated_result = str(a_number)
    return accumulated_result
