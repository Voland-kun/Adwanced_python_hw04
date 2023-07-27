def dict(**kwargs) -> {}:
    arg_dict = {}
    for key, value in kwargs.items():
        if value.__hash__:
            arg_dict[value] = key
        else:
            arg_dict[str(value)] = key
    return arg_dict


res = dict(a=1, b={2, 0}, c=3, d=[4, 5])
print(res)
