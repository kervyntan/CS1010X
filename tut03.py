def f(n):
    # Your code here
    if n < 3:
        return n
    else:
        return f(n - 1) + 2 * f(n - 2) + 3 * f(n-3)



def f_iter(n):
    # Your code here
    first = 2
    second = 1
    third = 0
    total = 0
    
    if n < 3:
        return n
    else:
        for i in range (3, n + 1) : # lets say we're finding n == 4, so is 3 - 5 (excl 5)
            # When n == 4, f(3) = f(2) + 2 * f(1) + 3 * f(0)
            total = first + 2 * second + 3 * third
            third = second # third = f(2)
            second = first # second = f(3)
            first = total # first = f(4)
            # f(3) = f(2) + 2 * f(1) + 3 * f(0)
            # third = f (1)  
            # second = f(2)
            # first = f(3)
            # f(4) = f(3) + 2 * f(2) + 3 * f(1)
            # third = f(2)
            # second = f(3)
            # first = f(4)
            # f(5) = f(4) + 2 * f(3) + 3 * f(2)
    return total


def is_fib(n):
    # Your code here
    first = 1
    second = 1
    third = 0
    if n == 0:
        return True
    elif n == 1:
        return True
    else:
        while third < n:
            third = first + second
            second = first
            first = third
            
        if third == n:
            return True
        else:
            return False


def make_fare(stage1, stage2, start_fare, increment, block1, block2):
    # Your code here
    distance = 0
    def taxi_fare(distance): 
        # distance in metres
        if distance <= stage1:
            return start_fare
        elif distance <= stage2:
            return start_fare + (increment * ceil((distance - stage1) / block1))
        else:
            return taxi_fare(stage2) + (increment* ceil((distance - stage2) / block2))
    # Returns a function that calculates the taxi fare using the values given
    return taxi_fare

