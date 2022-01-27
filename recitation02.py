#
# CS1010X --- Programming Methodology
#
# Mission 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.


#Big O means one-directional - Theta means both direction
# k ... fairness (speed of computer doesn't affect time complexity; adsorbed into k)
# n_o ... scalability

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

    if order == 0:
        return 0
    else:
        return 1 + order_size(order // 10)


def order_size_iter(order):

    count = 0
    n = len(str(order))
    
    for i in range (n):
        count+=1

    return count

### answers from recitation
def order_size(order):
    count = 0
    while order > 0:
        order = order // 10
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
            return order_cost(order // 10) + (combo * patty_price) + biggie_price
        else:
            return order_cost(order // 10) + combo * patty_price


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
# 5n ^2 + n < 6n^2 for n > 1
# 6n^2 is O(n ^ 2) as we can choose k=6

# 2(b) - O(n)
# sqrt(n)+ n < n + n = 2n
# 2n = O(n) we can choose k = 3

# 2(c) - O(3 ^ n * n ^2)
# 3^n n^2 < 3^n * n*2 (where n*2 cannot be removed/replaced by a constant k)
# 3^n n^ 2 =/ same way of finding order as 3^n + n^2

start_time = datetime.now()

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
    
end_time = datetime.now()

#3 - Runtime - O(2n) (trace code) - > O(n) (traced vertically, how many lines of code/operations) ,
# Space - O(n+1) = O(n) (observed horizontally - each line of code, how many actual spaces/items)

#4
def fact_iter(n):

    total = 1
    for i in range (n):
        total = total * n
        n-=1

    return total
#Running time - O(2n+1) (number of times of the loop) = O(n) , Space - O(3) = O(1) (how many things declared/used)
# Going through the loop (n-1) times, multiplied by constant (1), so O(n) * O(1)

#5
start_time = datetime.now()
def find_e(n):
    if n == 0:
        return 1
    else:
        return 1/fact(n) + find_e(n - 1)

end_time = datetime.now()
#Running time - O(n ^ 2), Space - O(2n) = O(n)
# Refer to google doc for code tracing
# space is reusable (eg. recursion, each step's space used can be reused for the next step)
# space used in calculating O(n) can be re-used in the calculation of fact(n-1), so we don't really need O(n) + O(n-1)... It is simply just O(n)

#Homework iterative find_e (time- O(n), space - O(1) )

#6
def is_divisible(n, x):
    return n % x == 0

def is_prime(num):


    if num > 1:

        for i in range (2,num):
            # for loop to num excludes num itself, and it excludes 1 since we're starting from 2
            if is_divisible(num, i) == True:
                return False
        else:
            return True


    else:
        return False
#Running time - O(n)
            
# for loop to num excludes num itself, and it excludes 1 since we're starting from 2, so any division along the way is wrong
        
    
print("--- %s seconds ---" % (end_time - start_time))

print(is_divisible(1000,13))

print(fact_iter(6))
        
print(order_cost(42))

print(order_size_iter(100))

print(is_prime(4))

    
 

