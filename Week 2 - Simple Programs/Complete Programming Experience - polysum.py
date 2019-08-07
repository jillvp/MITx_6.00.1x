# Grader
# 10.0/10.0 points (ungraded)

# A regular polygon has n number of sides. Each side has length s.

#    The area of a regular polygon is: 0.25∗𝑛∗𝑠2𝑡𝑎𝑛(𝜋/𝑛)
#    The perimeter of a polygon is: length of the boundary of the polygon

# Write a function called polysum that takes 2 arguments, n and s. This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.
# Hint: What to import?

# This is an optional exercise, but great for extra practice!

import math
def polysum(n, s):
    '''
    n = number of sides
    s = length of each side 
    returns: sum the area and square of the perimeter of the regular polygon. (rounded to 4 decimal places)
    '''
    area = (0.25*n*s*s) / (math.tan(math.pi/n))
    sum = area + (n*s) * (n*s)
    return round(sum, 4)
