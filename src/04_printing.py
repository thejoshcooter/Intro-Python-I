"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

print('x is % 2d, y is % 3f' % (10, 2.25))

# Use the 'format' string method to print the same thing

print('x is {}, y is {}, z is {}'.format(10, 2.25, "I like turtles!"))

# Finally, print the same thing using an f-string