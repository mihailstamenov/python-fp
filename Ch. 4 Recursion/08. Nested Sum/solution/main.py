def sum_nested_list(lst):
    total = 0
    for element in lst:
        if isinstance(element, list):
            total += sum_nested_list(element)
        else:
            total += element
    return total
