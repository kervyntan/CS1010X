#
# CS1010X --- Programming Methodology
#
# Mission 5 - Sidequest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *

##########
# Task 1 #
##########
draw_points (200 , unit_circle )
draw_points (200 , alternative_unit_circle )

# In unit_circle, as t increases, the distance between the next point and the previous point is the same.
# however in alternative_unit_circle, as t increases, the distance between the next point and the previous point increases.

# 2*pi*t is a linear statement, whereas 2*pi*t*t is a quadratic statement, with respect to t.
# If we differentiate both of these with respect to t, we get 2*pi and 4*pi*t. As we can see, the linear statement is a constant, thus the
# difference in distance between the next and previous point remains the same; however, in 4*pi*t, it varies and gets larger as t increases and approaches 1 from 0

##########
# Task 2 #
##########

# (a)
def spiral(t):
    return make_point(t * sin(2*pi*t), t * cos(2*pi*t))

draw_connected_scaled(1000, spiral)

# (b)
def heart(t):
    def left_half_spiral(t):
        return make_point(t * sin(2*pi*t), t * cos(2*pi*t))

    def right_half_spiral(t):
        return make_point(-t * sin(2*pi*t), t * cos(2*pi*t))
    
    return connect_rigidly(left_half_spiral, right_half_spiral)(t)

draw_connected_scaled(1000, heart)
