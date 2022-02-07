#
# CS1010X --- Programming Methodology
#
# Mission 2 - 2D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

########
# Task #
########

# You may submit up to 3 entries. Please update your entry number below.

# Entry 0 of 3
# ============
# Write your function here. It should return a rune.

def shift_one_left (num):
    # cast num to string
    # slice off the last part of the string
    # then append it to the beginning

    num = str(num)
    last_position = slice(0, 1)
    first_character = num[last_position]
    rest_of_number = num[1:len(num)]

    return int(rest_of_number + first_character)

#print(shift_one_left(23451))

def shift_left (num, n):
    final_num = str(num)

    for i in range (1, n + 1):
        first_character = final_num[0:1]
        rest_of_number = final_num[1:len(final_num)]
        final_num = rest_of_number + first_character

    return int(final_num)

# print(shift_left(12345, 2))

# do the recursive solution here
def shift_left_recursive (num, n):

    num = str(num)

    if n == 0:
        return num
    else:
        return (shift_left_recursive(num, n - 1)[1:len(num)]) + (shift_left_recursive(num, n - 1)[0:1])

# code tracing: return n == 2, n == 2 - shift...(num, n - 1) + num[0:1]
# return n == 1, shift...(num, 0) + num[0:1] -- return num[1, len(num)] + num[0,1]
# return n == 0, return num = 12345

print(shift_left_recursive(12345,2))

def shift_right (num, n):
    final_num = str(num)

    for i in range (1, n + 1):
        last_character = final_num[len(final_num) - 1:len(final_num)]
        rest_of_number = final_num[0:len(final_num) - 1]
        final_num = last_character + rest_of_number

    return int(final_num)

# print(shift_right(12345, 2))

def shift_right_recursive (num, n):

    num = str(num)

    if n == 0:
        return num
    else:
        return (shift_right_recursive(num, n - 1)[len(num) - 1:len(num)]) + (shift_right_recursive(num, n -1)[0:len(num) - 1])

print(shift_right_recursive(12345, 2))

#2
def nth_digit (n, num):
    digit = 0

    if n > len(str(num)): return None
    
    for i in range (n):
        digit = num % 10
        num = num // 10

    return digit

print(nth_digit(10, 12345))

def mth_digit (m, num):
    digit = 0
    num = str(num)

    for i in range (m):
        digit = num[i:i+1]

    return digit

print(mth_digit(3, 12345))

#3, careful of variable scoping !!! cannot define variables inside loops
#   they'll declare and remain the same value
def divisible_by_11(num):
    odd = 0
    even = 0
    count = 1
    if num == 0:
        return True
    else:
        num = str(num)
        for i in num:

            if count % 2 == 0 and count != 1:
                even += int(i)
            else:
                odd += int(i)
                
            count+=1
            
        if (odd - even) % 11 == 0:
            return True
        else:
            return False

    

print(divisible_by_11(33))

#4
def count_instances(num, seq):

    count = 0

    for i in range (0, len(seq)):
        if num == seq[i]:
            count+=1

    return count

print(count_instances(3, (1, 2, 3)))


#5

def concat(n, m):
    return str(n) + str(m)

print(concat(12345,67890))

#6

def replace_digit(n, d, r):
    n = str(n)

    for i in n:
        if int(i) == d:
            n = n.replace(i, str(r))


    return int(n)

print(replace_digit(31242154125, 1, 0))
        
#8

def count_change(amount, kinds_of_coins):
    
