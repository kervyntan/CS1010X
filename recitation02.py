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

print(order_size(12345678))

    
 

