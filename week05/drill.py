# (a,b) are function paramaters and only exist in the function scope
def swap(a, b):
    tmp = a # This a and b are in the function scope
    a = b
    b = tmp
     
    # Return statement to return variables
    return a,b


x = 3 # This "x" is in the global scope
y = 5 # This "y" is in the global scope


x,y = swap(a=x,b=y)


print("x is {}".format(x))
print("y is {}".format(y))









### DRILL

# DEFINING THE FUNCTION

# Simple function that prints
# Hello World
def hello_world():

    # Print is NOT the same as a return statement 
    print("Hello World")
    # return None 

#####################
# Standard logic for swapping two variables with a third variable

#tmp = a 
#a = b
#b = tmp

# CALLING THE FUNCTION

#hello_world()
#hello_world()
#hello_world()
#hello_world()

#################

# Key notes:

# sys.argv are not function parameters
# user input is not a function parameter
# function parameters are values that are explicitly passed to the function 



