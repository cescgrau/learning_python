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
