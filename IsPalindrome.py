def isPalindrome(number):

    number = str(number)
    
    for i in range (1, len(number)):

        first_digit = slice(i, i+1)
        last_digit = slice(len(number) - i - 1, len(number) - i)

        if number[first_digit] != number[last_digit]:
            return False
        
    return True

# first_digit = slice(i+1) = slice(1) = 1
# last_digit = slice(4 - 0) = slice(4) = 4
# if first_digit == 
#

print(isPalindrome(100000001111111))

def printPyramid (length):
    line_of_characters = '*'
    for i in range (length, 0, - 1):
        each_line = i * line_of_characters
        print(each_line)

print(printPyramid(5))


c = 5
def f(a):
    def g(a):
        d = a + c
        print(d)
    return g
f(3)(4)

p = 2
def h(y):
    def c(y):
        t = y + p
        print(t)
    return c
h(1)