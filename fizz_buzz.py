from domain.fizz_buzz.basic import map_basic
from domain.fizz_buzz.tools import map_fizz_buzz_for_a_range

if __name__ == '__main__':
    # print(map_fizz_buzz_number_for_a_range(start=1, end=100))
    # [print(item) for item in map_fizz_buzz_number_for_a_range(1,100)]
    for item in map_fizz_buzz_for_a_range(1, 100, function_chossed=map_basic):
        print(item)
