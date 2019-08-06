# Problem 3
# 15.0/15.0 points (graded)

# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.

# For example, if s = 'azcbobobegghakl', then your program should print

#    Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring.

# For example, if s = 'abcbcd', then your program should print

#    Longest substring in alphabetical order is: abc

# Note: This problem may be challenging. We encourage you to work smart.
# If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course.
# If you have time, come back to this problem after you've had a break and cleared your head.

#---------------------------CODE-------------------------------#
s = 'abcdefabcdehadhmqrz'

longest = s[0]
current = s[0]
# Both strings are initialized with the first letter

for c in s[1: ]:
# iterate over the input string, starting with the second character
    if c >= current[-1]:
        current += c
        if len(current) > len(longest):
            longest = current
    else:
        current = c
# if c does not fulfill requirement, we start with a new solution current = c
print('Longest substring in alphabetical order is: ' + longest)
# -------------------------------Result-------------------------------#
# Correct
