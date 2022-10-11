def has_separator_specification(a_string_with_numbers: str):
    return "//" == a_string_with_numbers[0:2]


def extract_separator(a_string_with_numbers: str) -> str:
    return a_string_with_numbers[2]
