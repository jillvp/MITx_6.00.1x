# Exercise: biggest

# (5/5 points)
# ESTIMATED TIME TO COMPLETE: 7 minutes

# Consider the following sequence of expressions:

# animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

# animals['d'] = ['donkey']
# animals['d'].append('dog')
# animals['d'].append('dingo')
# We want to write some simple procedures that work on dictionaries to return information.

# This time, write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values
# associated with it. If there is more than one such entry, return any one of the matching keys.

# Example usage:
# >>> biggest(animals)
# 'd'
# If there are no values in the dictionary, biggest should return None.

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    count = 0
    biggest = None
    for eachList in aDict:
        if len(aDict[eachList]) > count:
            count = len(aDict[eachList])
            biggest = eachList
    return biggest
    
# Correct
