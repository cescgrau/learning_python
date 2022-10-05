def add_two_lists_of_three_elements(first_list, second_list):
    if len(first_list) == len(second_list):
        string_indexes = list(range(len(first_list)))
        result_list=[]
        for index in string_indexes:
            result_list=result_list+[first_list[index]+second_list[index]]

        return result_list
    else:
        raise ValueError(f"first_list length: {len(first_list)} is not equal to second_list length: {len(second_list)}")