def is_multiple_of_five(a_number):
    return (a_number % 5) == 0


def is_multiple_of_three(a_number):
    return (a_number % 3) == 0


def map_from_integer_to_fizz_or_buzz(a_number):
    if is_multiple_of_three(a_number):
        return "fizz"
    if is_multiple_of_five(a_number):
        return "buzz"

    return str(a_number)


def map_fizz_buzz_number_for_a_range(start, end):
    list_result = []
    for index in range(start, end + 1):
        list_result = list_result + [map_from_integer_to_fizz_or_buzz(index)]
    return list_result
