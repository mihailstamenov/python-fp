def deduplicate_lists(lst1, lst2, reverse=False):
    res = set()

    for item in lst1:
        res.add(item)

    for item in lst2:
        res.add(item)

    res_lst = list(res)

    if reverse == True:
        return sorted(res_lst, reverse=True)
    return sorted(res_lst)
