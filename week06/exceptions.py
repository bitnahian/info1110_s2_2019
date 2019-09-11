"""
Function that takes in two integers and returns the value of the first parameter divided by the second parameter
"""
def divide(a, b):
    if not isinstance(a, int) or not isinstance(b, int) or a == 1110:
        raise ValueError("Wrong data type.")
    if b == 0:
        # Question: why might we want to do this?
        # What happens if we don't give ZeroDivisionError() any arguments?
        raise ZeroDivisionError("Attempted to divide {} by {}".format(a,b))
    return a / b # a % b 
a = input('Numerator: ')
b = input('Denominator: ')
try:
    ###
    # THIS CODE SEGMNET IS WHERE WE EXPECT THE ERROR TO HAPPEN
    x = int(a)
    y = int(b)
    n = divide(x, y)
    print('Result: {}'.format(n))
    ###
except ZeroDivisionError as e:
    print(e) # Why do we use the 'as' keyword here?
    #print("A ZeroDivisionError was raised")
    raise Exception("Programmer/User is stupid") # For exception chaining
except ValueError as e:
    print(e)
    print('What happened?')
except Exception:
    print('Will I ever trigger?')
finally:
    print('I always have the last laugh :D')

print("This is also always going to print")
