#1
j = 0
for i in range(10):
    if i >= 9: break
    if j == 8:
        j = j + 2
        continue
    j = j + 1


print(i, j)


#2
def sum_odd_n(n):
    """Sums first n odd integers starting from 1 (inclusive) using a for loop"""
    oddsum = 0
    
    for i in range (1, 2 * n, 2):
        oddsum+=i
        
    
    return oddsum

#print(sum_odd_n(5))


#4
def sum_odd_n(n):
    """Sums odd integers from 1 (inclusive) to n using recursion"""
    if n == 1:
        return 1
    else:
        return sum_odd_n(n - 1) + 2 * n - 1

print(sum_odd_n(5))

# sum_odd_n(1) = 1
# sum_odd_n(2) = sum_odd_n(1) + k = 4
# sum_odd_n(3) = sum_odd_n(2) + k = 9


#9

x, y = 1, 9
def foo(x, y):
    while y > x:
        y = y // 2
        x = x + 1

foo(x, y)

print(x)
print(y)

# variables defined out of scope of function remain as x and y


#10

def foo(n):
    if n == 0:
        return 0
    else:
        return 2 * n + foo(n - 1)

# n == 4, return 2 * 4 + foo(3) O(1)
# n == 3, return 2 * 3 + foo(2) O(1)
# n == 2, return 2 * 2 + foo(1) O(2n - 1)
# n == 1,
# return 2 * 4 + foo(3)
# return 2 * 4 + foo(3)


############################################## Tutorial #############################################

def foo1():
    i = 0
    result = 0 
    while i < 10:   
       result += i      
       i += 1   
    return result
print(foo1())

def foo2():
    i = 0
    result = 0
    while i < 10:
        if i == 3:
            break
        result += i
        i += 1
    return result
print(foo2())

def bar1():
    result = 0
    for i in range(10):
        result += i
    return result
print(bar1())

def bar2():
    result = 0
    for i in range(10):
        if i % 3 == 1:
            continue
        result += i
    return result
print(bar2())

def sum_even_factorials(n):
    # Returns the sum of factorials of even numbers 
    # that are less than or equal to n.
    factorial_sum = 0
    fact = 1
    
    if n == 0:
        return 1
        
    elif n % 2 == 0:
        
        for i in range (1, n + 1):
            fact = fact * i
            factorial_sum = factorial_sum + fact
            if (i == 1):
                i *= 2
            else:
                i += 2
        return factorial_sum

    else: 
        
        for i in range(1, n):
            fact = fact * i
            factorial_sum = factorial_sum + fact
            if (i == 1):
                i *= 2
            else:
                i += 2
            
        return factorial_sum
   
print(sum_even_factorials(6))
# n == 1, sum_even_factorials(0) == 1
# n == 2, sum_even_factorials(1) + k = 2 + 1
# n == 3, sum_even_factorials(2) + sum_even_factorials(1) + k = 3
#
#
#
#

def f(g):
    return g(2)

def square(x):
    return x ** 2

print(f(f))
