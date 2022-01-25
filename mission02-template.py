#
# CS1010X --- Programming Methodology
#
# Mission 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *
from mission01_template import *


###########
# Task 1a #
###########

def fractal(pic, n):
    # Fill in code here
    if n == 1:
        return pic
    else:
        return beside(pic, stack(fractal(pic, n-1), fractal(pic,n-1)))

# Test
# show(fractal(make_cross(rcross_bb), 3))
# show(fractal(make_cross(rcross_bb), 7))
# Write your additional test cases here
# show(fractal(make_cross(rcross_bb), 5))

###########
# Task 1b #
###########

def fractal_iter(pic, n):
    # Fill in code here
  
    final_pic = pic
    i = 1

    for i in range (n - 1):
        if i == n:
            return final_pic
        else:
            stack_pic = stack(final_pic, final_pic)
            final_pic = beside(pic, stack_pic)
            i+=1
            
    return final_pic

# Test
# show(fractal_iter(make_cross(rcross_bb), 3))
# show(fractal_iter(make_cross(rcross_bb), 7))
# Write your additional test cases here


###########
# Task 1c #
###########

def dual_fractal(pic1, pic2, n):
    # Fill in code here
        if n == 1:
            return pic1
        else:
            return beside(pic1, stack(dual_fractal(pic2, pic1, n-1), dual_fractal(pic2, pic1, n-1))) 

# Test
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 3))
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 4))
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1

###########
# Task 1d #
###########


def dual_fractal_iter(pic1, pic2, n):
    # Fill in code here
    final_pic = pic1
    even_pic = pic2
    i = n

    if n == 1:
        return final_pic

    elif n == 2:
        beside_stack_pic = beside(final_pic, stack(even_pic, even_pic))
        return beside_stack_pic
    
    else:

        while (i > 0):
            if i % 2 == 0:
                even_pic = beside(pic2, stack(final_pic,final_pic))
            else:
                final_pic = beside(pic1, stack(even_pic, even_pic))
            i-=1
                
    return final_pic
    

# Test
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 3))
show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 4))
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1

##########
# Task 2 #
##########

def steps(pic1, pic2, pic3, pic4):
    # Fill in code here
    mosaic_pic1 = mosaic(pic1, blank_bb, blank_bb, blank_bb)
    mosaic_pic2 = mosaic(blank_bb, pic2, blank_bb, blank_bb)
    mosaic_pic3 = mosaic(blank_bb, blank_bb, pic3, blank_bb)
    mosaic_pic4 = mosaic(blank_bb, blank_bb, blank_bb, pic4)
    return overlay(overlay(mosaic_pic4, mosaic_pic3), overlay(mosaic_pic2, mosaic_pic1))
    
    

# Test
# show(steps(rcross_bb, sail_bb, corner_bb, nova_bb))
 

