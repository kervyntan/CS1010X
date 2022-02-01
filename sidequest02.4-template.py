#
# CS1010X --- Programming Methodology
#
# Mission 2 - Side Quest 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

##########
# Task 1 #
##########

# Simplifed Order notations:

# 4^n * n^2
# Ans: O(4 ^ n)

# n * 3^n
# Ans: O(3 ^ n)

# 1000000000n^2
# Ans: O(n ^ 2)

# 2^n/1000000000
# Ans: O(2 ^ n)

# n^n + n^2 + 1
# Ans: O(n ^ n)

# 4^n + 2^n
# Ans: O(2 ^ (2 * n)) = O(2 ^ n)

# 1^n
# Ans: O(1)

# n^2
# Ans: O( n ^ 2 )

# Faster order of growth in each group:

# i. 4 ^ n * n ^ 2
# ii. 2^n/1000000000
# iii. n^n + n^2 + 1
# iv. n^2


##########
# Task 2 #
##########

# Code tracing: if n == 3, return 1 + bar(2) = 1 + 2 = 3
# n == 2, return 1 + bar(1) = 1 + 1 = 2
# n == 1, return 1 + bar(0) = 1 + 0
# n == 0, return 0

# Time complexity: O(2n + 1) = O(n)
# Space complexity: O(n)


##########
# Task 3 #
##########

def bar(n):
    if n == 0:
        return 0
    else :
        return n + bar(n - 1)
def foo(n):
    if n == 0:
        return 0
    else :
        return bar(n) + foo(n - 1)

# Time complexity of bar: O(2n + 1) = O(n)
# Time complexity of foo: O (n ^ 2)

# Space complexity of bar: O(n)
# Space complexity of foo: O(n)

def improved_foo(num):
    # Fill in code here
    total = 0
    addition = 0
    add_on = 0
    if num == 0:
        return 0
    else:
        for i in range (0, num + 1):
            addition = bar(i)  #bar(1) == 1
            total = add_on + addition # 1
            add_on = total # add_on == 1
            # addition == 1
            
    return total

# say i starts at 1, num == 3
# total += 1
# addition += 1
# total / foo == 1
# addition == bar(1) = 1
# add_on = total = 1
# i == 2, addition = bar(2) = 3
# total = 3 + add_on = 3 + 1 = 4

print(improved_foo(12))
print(foo(12))# 10


# improved_foo (3) - 
# Improved time complexity: O(n)
# Improved space complexity: O(1)
