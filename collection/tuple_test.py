# can't change tuple values
def tuple_test(values):
    try:
        values[0] = 'change value'
        for value in values:
            print(value)
    except TypeError:
        print('trying to modify tuple')


tuple_test(('do', 'it', 'right', 'always'))
