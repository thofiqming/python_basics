def find_duplicates(values):
    for val in values:
        if values.count(val) > 1:
            print(val)
            break


find_duplicates([1, 2, 3, 4, 4])


def find_value_occur(values):
    result = {}
    for val in values:
        result.setdefault(val, values.count(val))
    return result


res = find_value_occur([1, 2, 4, 3, 4])
print(res)
