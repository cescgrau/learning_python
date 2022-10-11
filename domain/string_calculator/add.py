from typing import Optional, List

from domain.string_calculator.tools import has_separator_specification, extract_separator


def add_internal(a_string_with_numbers: str, separators: Optional[List[str]] = None) -> int:
    separators = [",", "\n"] if separators is None else separators
    result = 0
    last_item_was_a_separator = ""
    for item in a_string_with_numbers:
        is_separator = True if item in separators else False
        if not is_separator:
            result += int(item)
        elif last_item_was_a_separator and is_separator:
            raise ValueError()
        last_item_was_a_separator = is_separator
    return result


def add(an_input: str) -> int:
    if has_separator_specification(an_input):
        return add_internal(an_input[5:], [extract_separator(an_input)])
    else:
        return add_internal(an_input)
