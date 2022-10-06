from domain.fizz_buzz.basic import is_multiple_of_five, is_multiple_of_three


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
    if not is_number_three_into_the_number(a_number) and not is_number_five_into_the_number(a_number):
        accumulated_result = str(a_number)
    return accumulated_result

def map_fizz_buzz_multiple_and_with_threes_and_fives_for_a_range(start, end):
    list_result = []
    for index in range(start, end + 1):
        list_result = list_result + [map_from_integer_to_fizz_and_buzz_extended(index)]
    return list_result


def is_number_three_into_the_number(a_number):
    return "3" in str(a_number)


def is_number_five_into_the_number(a_number):
    return "5" in str(a_number)


def map_from_integer_contains_three_to_fizz(a_number):
    if is_number_three_into_the_number(a_number):
        return "fizz"


def map_from_integer_contains_five_to_buzz(a_number):
    if is_number_five_into_the_number(a_number):
        return "buzz"
    return str(a_number)
