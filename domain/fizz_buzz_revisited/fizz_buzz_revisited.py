from domain.fizz_buzz_revisited.fizz_buzz_tools_revisited import is_multiple_of


def replace_if_contains_integer(an_integer):
    result = ""
    if "3" in str(an_integer):
        result += "fizz"
    if "5" in str(an_integer):
        result += "buzz"
    return result


def replace_if_contains_multiple_of(an_integer):
    result = ""
    if is_multiple_of(an_integer, divider=3):
        result += "fizz"
    if is_multiple_of(an_integer, 5):
        result += "buzz"
    return result


def reaching_the_list_with_integers_and_multiples(start=1, end=101):
    list_of_integers = []
    for index in range(start, end):
        list_of_integers=replace_if_contains_multiple_of(index)
        list_of_integers= replace_if_contains_integer(index)
    return result
