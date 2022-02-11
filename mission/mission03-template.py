#
# CS1010X --- Programming Methodology
#
# Mission 3
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

###########
# Task 1a #
###########

def compose(f, g):
    return lambda x:f(g(x))

def thrice(f):
    return compose(f, compose(f, f))

def repeated(f, n):
    if n == 0:
        return identity
    else:
        return compose(f, repeated(f, n - 1))

# Your answer here:
# n = 9

###########
# Task 1b #
###########

identity = lambda x: x
add1 = lambda x: x + 1
sq = lambda x: x**2

# (thrice(thrice)(add1)(6)) - thrice(
# (i) print(thrice(thrice)(add1)(6))]
# Explanation:
# Inner thrice function takes add1 as parameter, returning compose(add1, compose(add1, add1))
# Inner thrice then returns lambda x: x + 3
# Outer thrice takes lambda x : x + 3 as parameter, returning compose(x + 3, compose(x + 3, x + 3))
# This returns x + 27, since there are 9 counts of the function taking place i.e. f(f(f(f(f(f(f(f(f(
# Final result =  6 + 27 = 33


# (ii) print(thrice(thrice)(identity)(compose))
# Explanation: The memory address of compose will be returned.
# First thrice takes identity as a parameter, which takes in x and returns x
# Second thrice takes identity as a parameter as well, since there is no change in the output of the function
# Lastly, identity itself takes in compose function as an argument, and returns the address where the function is stored at since compose doesn't have any inputs

# (iii) print(thrice(thrice)(sq)(1))
# Explanation: 1
# First thrice takes in sq as a parameter, returns x ** 8
# Second thrice takes in lambda x : x ** 8 as the argument, which then repeats it 9 times, to x ** 8 ** 9 or x ** 134217728
# However, the input of square function is just 1, so answer remains as 1

# (iv) print(thrice(thrice)(sq)(2))
# Explanation: 2 ** 134217728
# First thrice takes in sq as a parameter, returns x ** 8
# Second thrice takes in lambda x : x ** 8 as the argument, which then repeats it 9 times, to x ** 8 ** 9 or x ** 134217728

###########
# Task 2a #
###########

def combine(f, op ,n):
    result = f(0)
    for i in range(n):
        result = op(result, f(i))
    return result

def smiley_sum(t):
    def f(x):
        if x == 0:
            return 1 / 3
        else:
            return (x + 1) ** 2
# f(3) = 2 * (9) + f(2)
# f(2) = 2 * (4) 

    def op(x, y):
        return int(x+ 2 * y)

    n  = t

    # Do not modify this return statement
    return combine(f, op, n)
# print(smiley_sum(3))

###########
# Task 2b #
###########

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def new_fib(n):
    def f(x):
        first = 0
        second = 1
        third = 0
        if x == 0 or x == 1:
            return x
        elif x == 2:
            return x
        else:
            return f(x - 1) + f(x - 2)
        

    def op(x, y):
        return x + y

    return combine(f, op, n+1)

print(fib(4))
print(new_fib(4))

# Your answer here:
