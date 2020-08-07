# Reading and understanding Error Messages!!!

# We need some code to create errors for us to look inot.
# For each example, make sure to fix the error
# in order to move on to the next!


# 1.  Synatx error
# SyntaxError: is the 'rule' of a language
# python follows ruls to let the computer
# know what to expect. if the rules are not followed
# the computer will not know what to do!

# 1a. 
a = 4
if a > 3
    print(a)
    
# 1b.
If a > 3:
    print(a)
    
# 1c.
for i i_n rnage(10):
    print(i)

# 2. NameError: is when a programming
# variable has not been defined.
# This causes the computer to not
# know what, or where the data is.

# 2a. 
print(z)

# 2b.
for i in range(5):
    print(var)

# 2c.
print("my name is {}.".format(name))

# 3. ZeroDivisionError: because we cannot
# yet divide by 0...

3a.
print(1 /0)

# 4. IndexError: When a computer tries to read
# value from a data structure at a position
# outside of its size

# 4a.
listy = [1, 2, 3, 4]
print(listy[4])

# 4b.
for i in rnage(4):
    print(listy[i])

# 5. ModuleNotFoundError: when the program tries to
# 'import' python tools that are NOT downloaded

# 5a.
import numpi

# 6. RecursionError: recursion is when a function calls itself in hopes
# for a different outcome. if a computer calls too many functions at
# once, the program will crash.

# 6a.
def rec(a):
    if a != 1:
        rec(a + 1)   #would it be better is it was minus 1?
rec(2)




