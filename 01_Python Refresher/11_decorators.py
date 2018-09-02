import functools

def myDecorator(func):
    @functools.wraps(func)
    def secondMethod():
        print("Will Print FIrst")
        func()
        print("Will Be printed Last")
    return secondMethod

@myDecorator
def myfunction():
    print("Hellllo")

myfunction()
