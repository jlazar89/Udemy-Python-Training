# working with args
# it works as list and will return the sum
# it can be n number of arguments
def addition_simplified(*args):
    return sum(args)

print(addition_simplified(7,7,7,7,7,7,7,7,7,7))

# kwargs can have named paramters
# kwargs is Keyword arguments
def kwargs_example(*args, **kwargs):
    print(args)
    print(kwargs)

kwargs_example(12,45,78, name='Jeffy', location='India')
