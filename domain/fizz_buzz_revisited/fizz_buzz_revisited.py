def is_multiple_of(a_integer: int, divider: int) -> int:
    return a_integer % divider == 0


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


def replacing_integers(start, end):
    list_of_integers = []
    for an_integer in range(start, end):
        result = ""
        if "3" in str(an_integer):
            result += "fizz"
        if "5" in str(an_integer):
            result += "buzz"
        if not "3" in str(an_integer) and not "5" in str(an_integer):
            result=an_integer
        list_of_integers.append(result)
    return list_of_integers


def reaching_the_list_with_integers_and_multiples(start=1, end=101):
    result = list(zip(replacing_multiple_of(start, end), replacing_integers(start, end)))
    return result
