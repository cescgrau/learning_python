def is_multiple_of_five(a_number):
    return (a_number % 5) == 0


def is_multiple_of_three(a_number):
    return (a_number % 3) == 0


def is_number_three_into_the_number(a_number):
    return "3" in str(a_number)


def is_number_five_into_the_number(a_number):
    return "5" in str(a_number)

def map_fizz_buzz_for_a_range(start, end, function_chossed):
    list_result = []
    for index in range(start, end + 1):
        list_result = list_result + [function_chossed(index)]
    return list_result
