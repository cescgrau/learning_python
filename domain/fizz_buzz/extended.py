from domain.fizz_buzz.tools import is_multiple_of, is_character_into


def map_from_integer_to_fizz_and_buzz_extended(a_number):
    accumulated_result = ""
    if is_character_into(character="3", a_number=a_number):
        accumulated_result += "fizz"
    if is_character_into(character="5", a_number=a_number):
        accumulated_result += "buzz"
    if is_multiple_of(multiple=5, a_number=a_number):
        accumulated_result += "buzz"
    if is_multiple_of(multiple=3, a_number=a_number):
        accumulated_result += "fizz"
    if accumulated_result == "":
        accumulated_result = str(a_number)
    return accumulated_result
