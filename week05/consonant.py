"""
Function that takes in parameter ch and returns a boolean value for whether ch is a consonant or not
"""
def consonant(ch):
    # complete this function so it returns True iff `ch` is a consonant letter
    
    if len(ch) > 1:
        return False

    if ch == "b" or ch == "c" or ch == "d" or ch == "f" or ch == "g" or ch == "h" or ch == "j" or ch == "k" or ch == "l" or ch == "m" or ch == "n" or ch == "p" or ch == "q" or ch == "r" or ch == "s" or ch == "t" or ch =="v" or ch == "w" or ch == "x" or ch == "y" or ch == "z":
        return True
    
    else:
        return False

b = consonant('d') # True
print(b)
b = consonant('e') # False
print(b)
b = consonant('wool') # False
print(b)
