def romans_mapping(an_integer: str):
    translation = ""
    mapping = {
        0: {
            "0": "",
            "1": "I",
            "2": "II",
            "3": "III",
            "4": "IV",
            "5": "V",
            "6": "VI",
            "7": "VII",
            "8": "VIII",
            "9": "IX"
        },
        1: {
            "0": "",
            "1": "X",
            "2": "XX",
            "3": "XXX",
            "4": "XL",
            "5": "L",
            "6": "LX",
            "7": "LXX",
            "8": "LXXX",
            "9": "XC"
        },
        2: {
            "0": "",
            "1": "C",
            "2": "CC",
            "3": "CCC",
            "4": "CD",
            "5": "D",
            "6": "DC",
            "7": "DCC",
            "8": "DCCC",
            "9": "CM"
        },
        3: {
            "1": "M",
            "2": "MM",
            "3": "MMM"
        }}
    number_of_characters = len(an_integer)
    an_integer_reversed = an_integer[::-1]
    for index in range(0, number_of_characters):
        current_character = an_integer_reversed[index]
        translation = mapping[index][current_character] + translation
    return translation
