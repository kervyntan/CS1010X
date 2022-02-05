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

def square_of_runes (rune, n):
    resized_rune = scale(0.5, rune)

    if n == 1:
        return resized_rune
    if n == 2:
        top_row = beside(resized_rune, resized_rune)
        return stack(top_row, top_row)
    else:
        rotated_left_rune = quarter_turn_left(rune)
        stacked_runes = stackn( n - 2, rotated_left_rune )
        rotated_stacked_runes = quarter_turn_right (stacked_runes)
        top_stack = stack(rotated_stacked_runes, rotated_stacked_runes)

        for i in range (1, n - 4):
            top_stack = stack_frac((n - 2) / n, top_stack, rotated_stacked_runes)

        original_orientation_bottom_stack = quarter_turn_right (stacked_runes)
        combined_stack = stack_frac( (n - 1) / n, top_stack, original_orientation_bottom_stack)

        if n == 3:
            combined_stack = rune
        if n == 4:
            combined_stack = stack(rotated_stacked_runes, rotated_stacked_runes)
        
        middle = stack_frac(1 / (n - 1), quarter_turn_right(stacked_runes), combined_stack)
        complete_middle = stack_frac ( (n-1) / n , middle, quarter_turn_right(stacked_runes))
        rotated_left_picture = quarter_turn_left(complete_middle)
        complete_side = quarter_turn_left(stackn(n, rune))
        top_half_completed_picture = stack_frac( 1 / (n - 1) , complete_side, rotated_left_picture)
        rotated_left_completed_picture = stack_frac ( (n - 1) / n, top_half_completed_picture, complete_side)

        return quarter_turn_right(rotated_left_completed_picture)
    
show(square_of_runes(nova_bb, 4))



