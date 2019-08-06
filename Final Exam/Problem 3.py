# Problem 3
# 10.0/10.0 points (graded)

# Write a function is_triangular that meets the specification below. A triangular
# number is a number obtained by the continued summation of integers starting from 1.
# For example, 1, 1+2, 1+2+3, 1+2+3+4, etc., corresponding to 1, 3, 6, 10, etc., are triangular numbers.

# def is_triangular(k):
#    """
#    k, a positive integer
#    returns True if k is triangular and False if not
#    """
#    #YOUR CODE HERE

#Paste your entire function, including the definition, in the box below. Do not leave any debugging print statements.

#---------------------------CODE-------------------------------#
def is_triangular(k):
   """
   k, a positive integer
   returns True if k is triangular and False if not
   """
   num = 1
   triangularNo = 0
   while triangularNo < k:
       triangularNo += num
       num += 1
   if triangularNo == k:
       return True
   return False
# -------------------------------Result-------------------------------#
# Correct

# Test cases
print(is_triangular(1))
print(is_triangular(3))
print(is_triangular(6))
print(is_triangular(10))
print(is_triangular(4))
# -----------------------
