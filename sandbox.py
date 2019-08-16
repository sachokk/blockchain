def test_function(callback, *args):
    res = callback(*args)
    print(f' result: {res:^20.0f}')

def plus(a , b):
    return a + b

#test_function(lambda a, b: a + b, 51, 62)

my_list = [1,2,3,4,5]

print('-'.join([str(el) for el in my_list]))
