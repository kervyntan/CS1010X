#
# CS1010X --- Programming Methodology
#
# Mission 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.


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
        
print(order_cost_iter(12))

    
 

