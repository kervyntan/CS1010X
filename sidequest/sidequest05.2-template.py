#
# CS1010X --- Programming Methodology
#
# Mission 5 - Sidequest 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph_connect_ends import *

##########
# Task 1 #
##########

def kochize(level):
    if level == 0:
        return unit_line
    else:
        first = kochize(level - 1)
        second = rotate( pi / 3) ( kochize(level - 1) )
        third = rotate (- pi / 3)( kochize(level - 1) )
        first_second = connect_ends(first, second)
        combined_3_together = connect_ends(first_second, third)
        combined_4_together = connect_ends(combined_3_together, first)
        return put_in_standard_position(combined_4_together)

def show_connected_koch(level, num_points):
    draw_connected(num_points, kochize(level))

#show_connected_koch(0, 4000)
show_connected_koch(2, 4000)

##########
# Task 2 #
##########

def snowflake():
    "your answer here"

#draw_connected_scaled(10000, snowflake())
