def is_multiple_of(multiple, a_number):
    return a_number % multiple == 0


def map_fizz_buzz_for_a_range(start, end, function_chossed):
    list_result = []
    for index in range(start, end + 1):
        list_result = list_result + [function_chossed(index)]
    return list_result


def is_character_into(character, a_number):
    return character in str(a_number)
