#
# CS1010X --- Programming Methodology
#
# Mission 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

import time
from datetime import datetime

def biggie_size(combo):
    return combo + 4

def unbiggie_size(combo):
    return combo - 4

def is_biggie_size(combo):

    if combo < 5:
        return False
    else:
        return True

def combo_price(combo):

    if combo > 4:
        return combo * 1.17 + 0.50
    else:
        return combo * 1.17

def empty_order():
    return 0

def add_to_order(order, combo):
    return str(order) + str(combo)

def order_size(order):
    
    count = 1
    #if digit is 0, then stop
    if order == 0:
        return 0
    else:
        return count + order_size(order // 10)


def order_size_iter(order):

    i = 1
    count = 0
    n = len(str(order))
    
    for i in range (n):
        count+=1

    return count

####### Session 2

def order_cost(order):

    patty_price = 1.17
    biggie_price = 0.50
    combo = order % 10

    if order == 0:
        return 0
    else:
        if combo > 4:
            return order_cost(order // 10) + (combo * 1.17) + 0.50
        else:
            return order_cost(order // 10) + combo * 1.17


    # order 123
    #price of combo 3 -> order_cost(123 // 10) + 3 * 1.17
    #price of combo 2 -> order_cost(12 // 10) + 2 * 1.17
    #price of combo 1 -> order_cost(1 // 10) + 1 * 1.17
    #price of 0 -> return 0

def order_cost_iter(order):
    sum = 0
    patty_price = 1.17
    biggie_price = 0.50
    price = 0
    n = len(str(order))
    i = 0
    for i in range (n):
        combo = order % 10
        if combo < 5:
            price = price + combo * 1.17
            order = order // 10
        else:
            price = price + combo * 1.17 + 0.50
            order = order // 10

    return price

def add_orders(order1, order2):
    return str(order1) + str(order2)

# 2(a) - O(n ^ 2)
# 2(b) - O(n)
# 2(c) - O(n)

start_time = datetime.now()

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
    
end_time = datetime.now()

#3 - Runtime - 0ms, Space - O(n)

#4
def fact_iter(n):

    i = 1
    total = 1
    for i in range (n):
        total = total * n
        n-=1

    return total

#5
start_time = datetime.now()
def find_e(n):
    if n == 0:
        return 1
    else:
        return 1/fact(n) + find_e(n - 1)

end_time = datetime.now()
#Running time - 0ms, Space - O(n)

#6
def is_divisible(n, x):
    return n % x == 0

def is_prime(num):


    if num > 1:

        for i in range (2,num):
            if is_divisible(num, i) == True:
                return False
        else:
            return True


    else:
        return False
            
        
        
    
print("--- %s seconds ---" % (end_time - start_time))

print(is_divisible(1000,13))

print(fact_iter(6))
        
print(order_cost(42))

print(is_prime(10))

    
 

