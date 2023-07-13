
def test_args_kwargs(arg1, arg2, arg3):
    print(f'arg1 {arg1}')
    print(f'arg2 {arg2}')
    print(f'arg3 {arg3}')


args = ('two', 3,5)
kwargs = {'arg3': 3, 'arg2': 'two', 'arg1':5}

test_args_kwargs(*args)
test_args_kwargs(**kwargs)