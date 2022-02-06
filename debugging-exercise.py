x = 10
y = 20

def foo(x, y, z):
    return x * y / bar(z)

def bar(x):
    if x > 5:
        return x
    else:
        return 0

print(foo(x, y, 12))
z = 4
print(foo(x, y, z))
print(bar(3))