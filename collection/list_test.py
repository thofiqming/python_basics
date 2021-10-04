def sort_list(values):
    values.sort()
    print(values)


sort_list([1, 2, 5, 6])


def print_index_and_values(values):
    for index, value in enumerate(values, start=1):
        print(index, value)


print_index_and_values(['do', 'it', 'right', 'always'])


def join_list_with_comma_seperated_values(values):
    print(','.join(values))


join_list_with_comma_seperated_values(['do', 'it', 'right', 'always'])
