from math import sin, pi

def isPalindrome(number):

    number = str(number)
    
    for i in range (1, len(number)):

        first_digit = slice(i, i+1)
        last_digit = slice(len(number) - i - 1, len(number) - i)

        if number[first_digit] != number[last_digit]:
            return False
        
    return True

# first_digit = slice(i+1) = slice(1) = 1
# last_digit = slice(4 - 0) = slice(4) = 4
# if first_digit == 
#

print(isPalindrome(100000001111111))

def printPyramid (length):
    line_of_characters = '*'
    for i in range (length, 0, - 1):
        each_line = i * line_of_characters
        print(each_line)

print(printPyramid(5))



def deriv(g):
    dx = 0.00001 # a small difference
    return lambda x: (g(x + dx) - g(x)) / dx

cos = deriv(sin)
print(cos(pi / 4))

def compose(f, g):
    return lambda x: f(g(x))

foo = lambda x: x+1
bar = compose(foo, foo)
print(compose(bar, bar)(10))

def compose(f, g):
    return lambda x: f(g(x))

def add1(x):
    return x + 1

def times3(x):
    return x * 3


three_x_plus_1 = lambda x: compose(add1, times3)(x)
print(three_x_plus_1)
