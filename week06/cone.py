import math

"""
Write a function, cone(radius, height) , that returns the volume of a cone based on the given
function parameters.
"""
def cone(radius, height):
    if ((not isinstance(radius, int) 
            and not isinstance(radius, float)) or
            (not isinstance(height, int)
            and not isinstance(height, float))):
        raise TypeError("Error: parameters radius and height must be numeric.")
    if radius < 0:
        raise ValueError("Error: radius must be positive.")
    if height < 0:
        raise ValueError("Error: height must be positive.")


    volume = math.pi * (radius ** 2) * (height/3)
    return volume


print(cone("hello", 3)) # Returns 12.566
    
