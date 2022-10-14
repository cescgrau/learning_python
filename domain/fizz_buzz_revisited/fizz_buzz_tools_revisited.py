def a_returning_a_list_of_integers(start: int, end: int):
    list_of_integers = []
    for an_integer in range(start, end):
        list_of_integers = list_of_integers + [an_integer]
    return list_of_integers


def is_multiple_of(a_integer: int, divider: int) -> int:
    return a_integer % divider == 0
