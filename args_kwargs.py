def print_args_kwargs(*args, **kwargs):
    print(args)  # tuple
    print(kwargs)  # dictionary


print_args_kwargs('do', 'it', quote='do it right')
# ('do', 'it')
# {'quote': 'do it right'}
