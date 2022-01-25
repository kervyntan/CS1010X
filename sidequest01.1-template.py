#
# CS1010X --- Programming Methodology
#
# Mission 1 - Side Quest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

##########
# Task 1 #
##########

def egyptian(a, b):
     
     return border
# Test
# show(egyptian(nova_bb, 5))

def egypt (pic, n):
     rotated_left_rune = quarter_turn_left(pic)
     side_of_middle = stackn(n - 2, rune)
     middle = stack_frac(1 / (n - 1), quarter_turn_right(side_of_middle), pic)

     complete_middle = stack_frac ( (n-1) / n , middle, quarter_turn_right(side_of_middle))

     rotated_left_picture = quarter_turn_left(complete_middle)

     complete_side = quarter_turn_left(stackn(n, pic))

     top_half_completed_picture = stack_frac( 1 / (n - 1) , complete_side, rotated_left_picture)

     rotated_left_completed_picture = stack_frac ( (n - 1) / n, top_half_completed_picture, complete_side)

     return quarter_turn_right(rotated_left_completed_picture)



show(egypt(nova_bb,5))
