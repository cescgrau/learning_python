def romans_mapping(an_integer: str):
    translation = ""
    number_of_characters = length_of_numeral(an_integer)
    last_character_of_string = number_of_characters - 1
    for index in range(number_of_characters):
        if index == 0:
            if an_integer[last_character_of_string - index] == "1":
                translation = "I"
            elif an_integer[last_character_of_string - index] == "2":
                translation = "II"
            elif an_integer[last_character_of_string - index] == "3":
                translation = "III"
            elif an_integer[last_character_of_string - index] == "4":
                translation = "IV"
            elif an_integer[last_character_of_string - index] == "5":
                translation = "V"
            elif an_integer[last_character_of_string - index] == "6":
                translation = "VI"
            elif an_integer[last_character_of_string - index] == "7":
                translation = "VII"
            elif an_integer[last_character_of_string - index] == "8":
                translation = "VIII"
            elif an_integer[last_character_of_string - index] == "9":
                translation = "IX"
        if index == 1:
            if an_integer[last_character_of_string - index] == "1":
                translation = "X" + translation
            elif an_integer[last_character_of_string - index] == "2":
                translation = "XX" + translation
            elif an_integer[last_character_of_string - index] == "3":
                translation = "XXX" + translation
            elif an_integer[last_character_of_string - index] == "4":
                translation = "XL" + translation
            elif an_integer[last_character_of_string - index] == "5":
                translation = "L" + translation
            elif an_integer[last_character_of_string - index] == "6":
                translation = "LX" + translation
            elif an_integer[last_character_of_string - index] == "7":
                translation = "LXX" + translation
            elif an_integer[last_character_of_string - index] == "8":
                translation = "LXXX" + translation
            elif an_integer[last_character_of_string - index] == "9":
                translation = "XC" + translation
        if index == 2:
            if an_integer[last_character_of_string - index] == "1":
                translation = "C" + translation
            elif an_integer[last_character_of_string - index] == "2":
                translation = "CC" + translation
            elif an_integer[last_character_of_string - index] == "3":
                translation = "CCC" + translation
            elif an_integer[last_character_of_string - index] == "4":
                translation = "CD" + translation
            elif an_integer[last_character_of_string - index] == "5":
                translation = "D" + translation
            elif an_integer[last_character_of_string - index] == "6":
                translation = "DC" + translation
            elif an_integer[last_character_of_string - index] == "7":
                translation = "DCC" + translation
            elif an_integer[last_character_of_string - index] == "8":
                translation = "DCCC" + translation
            elif an_integer[last_character_of_string - index] == "9":
                translation = "CM" + translation
        if index == 3:
            if an_integer[last_character_of_string - index] == "1":
                translation = "M" + translation
            if an_integer[last_character_of_string - index] == "2":
                translation = "MM" + translation
            if an_integer[last_character_of_string - index] == "3":
                translation = "MMM" + translation
        translation = translation
    return translation


def length_of_numeral(an_integer: str):
    return len(an_integer)


def translate_numeral(an_integer: str) -> str:
    result = romans_mapping(an_integer)
    return result
