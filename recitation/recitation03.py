def sum ( term , a , next , b ):
    if a > b :
        return 0
    else :
        return term ( a ) + sum( term , next ( a ) , next , b )
    
def fold ( op , f , n ):
    if n == 0 :
        return f ( 0 )
    else :
        return op ( f ( n ) , fold ( op , f , n - 1 ))

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
# 18 -> g(3) + 3

x = 4
def foo( x ):
    return x ( 3 )
print(foo ( lambda x : x + 1 )
)
# 4

x = 5
def bar(x , y ):
    return y ( x )
print(bar (4 , lambda x : x ** 2 )
)

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

print(my_sum(5))

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

print(my_sum_iter(5))
#iter - O(1) for space, O(n) for time

def my_sum_HOF (n):
    return sum(lambda x : x * (x + 1), 1, lambda x : x + 1, n)

print(my_sum_HOF(5))

print(sum(lambda x : x, 1, lambda x : x + 1, 15))

def sum_iter(start, end, term):
    sum = 0
    for i in range (start, end + 1):
        sum = sum + term(i)

    return sum

print(sum_iter(1, 15, lambda x: x))


def my_sum_fold (n):
    return fold (lambda x,y : x + y, lambda x : x ** 2 + x, n)

print(my_sum_fold(5))

def calc_integral(f, a, b, n):
    # Put your code here #
    h = (b - a) / n
    front = h / 3
    sum = f(a)
    
    for i in range (1, n + 1):
        if i % 2 == 0 and i != n:
            sum = sum + 2 * f(a + i * h)
        elif i % 2 != 0 and i != n:
            sum = sum + 4 * f(a + i * h)
        elif i == n:
            sum = sum + f(a + i * h)
    
    return front * sum



print(calc_integral(lambda x: x*x*x, 0, 1, 100))
#0.25000000000000006

def g(k):
    return fold(lambda x, y: x * y, lambda x : x - (x + 1) ** 2 ,k)

print(g(3))


def accumulate(combiner, base, term, a, next, b):
    if a > b:
        return base
    else:
        return combiner(term(a),(accumulate(combiner, base, term, next(a), next, b)))

def make_point(x, y):
    #Your code here
    return str(x) + str(y)

def x_point(p):
    #Your code here
    return int(p[0:1])
    
def y_point(p):
    #Your code here
    return int(p[1:2])

#For running public test case, do not delete
p1 = make_point(2, 3)
x_point(p1)

def make_segment(p1, p2):
    #Your code here
    return str(p1) + str(p2)
    
def start_segment(s):
    #Your code here
    return s[0:2]

def end_segment(s):
    #Your code here
    return s[2:4]

p1 = make_point(2, 3)
p2 = make_point(5, 7)

print(make_segment(p1,p2))

def accumulate_iter(combiner, null_value, term, a, next, b):

    result = null_value

    while a <= b:

        result = combiner(term(a), result)

        a = next(a)

    return result

print(accumulate_iter(lambda x, y: x * y, 1, lambda x: x**3 + 1, 0, lambda x: x+2, 5))
print(accumulate(lambda x, y: x * y, 1, lambda x: x**3 + 1, 0, lambda x: x+2, 5))

