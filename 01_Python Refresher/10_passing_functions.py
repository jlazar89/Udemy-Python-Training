def methodception(another):
    return another()

def addNumbers():
    return 36 + 77

print(methodception(addNumbers))

# Lamba Functions
print(methodception(lambda: 35 + 87))

(lambda x: x*5)(5)
# is the same as below
def f(x):
    return x * 3 
