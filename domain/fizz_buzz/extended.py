from domain.fizz_buzz.tools import is_multiple_of_five, is_multiple_of_three, is_number_three_into_the_number, \
    is_number_five_into_the_number


def map_from_integer_to_fizz_and_buzz_extended(a_number):
    accumulated_result = ""
    if is_number_three_into_the_number(a_number):
        accumulated_result += "fizz"
    if is_number_five_into_the_number(a_number):
        accumulated_result += "buzz"
    if is_multiple_of_five(a_number):
        accumulated_result += "buzz"
    if is_multiple_of_three(a_number):
        accumulated_result += "fizz"
    if accumulated_result == "":
        accumulated_result = str(a_number)
    return accumulated_result
