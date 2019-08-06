# Problem 1
# 10.0/10.0 points (graded)

# Assume s is a string of lower case characters.

# Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
# For example, if s = 'azcbobobegghakl', your program should print:

# Number of vowels: 5

#---------------------------CODE-------------------------------#
string = "qwertyyuiopsaskdmnxi"
numVowels = 0

for char in string:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        numVowels += 1
        
print('Number of vowels: ' + str(numVowels))
# -------------------------------Result-------------------------------#    
# Correct
