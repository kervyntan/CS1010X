def sum ( term , a , next , b ):
    if a > b :
        return 0
    else :
        return term ( a ) + sum( term , next ( a ) , next , b )

###########################################

x = 2
def f():
    x = 5
    y = x + 5

    return x + y
f () + x
# 17

x = 2
y = 3
def g( x ):
    y = x + 5
    x = 7
    return x + y

print(g ( y )+ y)
# 18 - g(3) + 3

x = 4
def foo( x ):
    return x ( 3 )
print(foo ( lambda x : x + 1 ))
# 4

x = 5
def bar(x , y ):
    return y ( x )
print(bar (4 , lambda x : x ** 2 ))

# 16

def my_sum(n):
    if n == 1:
        return n * 2
    if n == 2:
        return n * (n + 1) + n 
    else:
        return my_sum(n - 1) + n * (n + 1)
# my_sum(3) = my_sum(2) + ... = 8 + 12 = 20
# my_sum(2) = my_sum(1) + ... 2 + 6 = 8
# my_sum(1) = 2

print(my_sum(3))

#recursive, O(2n) for time, O(n) for space

def my_sum_iter(n):
    first = 1
    second = 2
    sum = 0

    for i in range (1, n + 1):
        sum = sum + first * second
        first +=1
        second +=1

    return sum

print(my_sum_iter(4))
#iter - O(1) for space, O(n) for time

def my_sum_HOF (n):
    return sum(lambda x : x ** 2 + x, 1, lambda x : x + 1, n)

print(my_sum_HOF(3))

print(sum(lambda x : x, 1, lambda x : x + 1, 15))

def sum_iter(start, end, term):
    sum = 0
    for i in range (start, end + 1):
        sum = sum + term(i)

    return sum

print(sum_iter(1, 15, lambda x: x))
