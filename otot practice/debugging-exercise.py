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
        