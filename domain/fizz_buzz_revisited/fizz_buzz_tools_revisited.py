def a_returning_a_list_of_integers(start: int, end: int):
    list_of_integers = []
    for an_integer in range(start, end):
        list_of_integers = list_of_integers + [an_integer]
    return list_of_integers


def replacing_multiple_of(start, end):
    list_of_integers = []
    for an_integer in range(start, end):
        result = ""
        if is_multiple_of(an_integer, divider=3):
            result += "fizz"
        if is_multiple_of(an_integer, 5):
            result += "buzz"
        if not is_multiple_of(an_integer, divider=3) and not is_multiple_of(an_integer, divider=5):
            result = an_integer
        list_of_integers.append(result)
    return list_of_integers


def is_multiple_of(a_integer: int, divider: int) -> int:
    return a_integer % divider == 0
