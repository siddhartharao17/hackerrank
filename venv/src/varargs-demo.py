# This program demonstrates the use of *args which is called variable non-keyworded arguments.
# This is used when you suspect that a function might accept multiple arguments rather than
# restricting it to just n number of args at compile time.

# Example of fixed args at compile time
# def multiply(x,y):
#     print(x*y)
#
# multiply(5,4)
# multiply(3,5,4) # This will give an error saying "TypeError: multiply() takes 2 positional arguments but 3 were given"

# We want this function to accept multiple arguments at runtime and tell the compiler that we do not know in the beginning
# about the number of arguments we want to give.

# Example of variable args at runtime
def multiply(*args):
    # now we don't have x and y to simply multiply them so we need to iterate through
    # the list of args that are comma separated.
    product=1
    for number in args:
        product=product*number
    print(product)

multiply(5,4)
multiply(5,4,4,6)
multiply(5,4,3)
multiply(5,4,5,2,8,9)
multiply(5,4,6,12)