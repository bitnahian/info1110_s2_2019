"""
Function that prints the mean of the numbers in list nums and returns a tuple
- The tuple's first element is the index of the number furthest from the mean
- The tuple's second element is the number furthest from the mean
"""
def average(ls):

    # Check for errors in your variables before you use them
    if type(ls) != list:
        print("Wrong type")
        return

    if len(ls) < 1:
        print("List size is 0")
        return


    # Printing the mean
    mean = calculate_mean(ls)
    print(mean)
    
    index, num = find_furthest(ls, mean)

    return index, num


def calculate_mean(ls):
    sum_val = 0
    
    i = 0
    # Standard idiom to loop over a list
    while i < len(ls):
        sum_val += ls[i]
        i += 1

    mean = sum_val/len(ls)
    
    return mean

def find_furthest(ls, mean):
    i = 0
    # Assume the first element of the list to be the furthest candidate
    furthest_index = 0
    furthest_num = ls[0]
    max_diff = abs(ls[0] - mean)

    while i < len(ls):

        if abs(ls[i] - mean) > max_diff:
            max_diff = abs(ls[i] - mean)
            furthest_index = i
            furthest_num = ls[i]
        
        i+= 1
    
    return furthest_index, furthest_num



ls = [5, 3, 2, 4, 10]

# The call to function `average` will:
# - Print the mean of the numbers in `ls`: 4.8
# - Return the tuple (4, 10)

tup = average(ls) # prints '4.8'
print(tup[0], tup[1]) # 4, 10

spam = [5, -25]
tup = average(spam) # prints '-10'
print(tup[0], tup[1]) # 1, -25

ham = [3.1415]
tup = average(ham) # prints '3.1415'
print(tup[0], tup[1]) # 0, 3.1415

eggs = []
tup = average(eggs) # prints 'The average doesn't exist!'
print(tup) # None (if the list is empty, function `average` returns None)
