#
# Example file for variables
#

# Declare a variable and initialize it
f = 0
print(f)


# # re-declaring the variable works
f = "abc"
print(f)


# # ERROR: variables of different types cannot be combined
# print("this is a string" + 123) #gives error
print("this is a string" + str(123)) #works fine

# Global vs. local variables in functions
def someFunction():
    global f
    f = "def"
    print(f)

someFunction()
print(f)

del f #deletes the f variable
print(f) #throws error because variable f no longer exists
