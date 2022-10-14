from domain.fizz_buzz_revisited.fizz_buzz_tools_revisited import replacing_multiple_of


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
