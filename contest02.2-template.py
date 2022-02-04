#
# CS1010X --- Programming Methodology
#
# Mission 2 - 2D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

########
# Task #
########

# You may submit up to 3 entries. Please update your entry number below.

# Entry 1 of 3
# ============
# Write your function here. It should return a rune.

def huge_cross (rune, n):

    if n == 1:
        return rune
    else:
        pic = rune
        new_pic = rune
        final_pic = rune
        for i in range (1, n):
            new_pic = stack(pic, new_pic)
            new_pic = quarter_turn_left(new_pic)

        return new_pic
         


show(huge_cross(sail_bb, 5))



