"""
Function that takes in a list and swaps the first and last element of the list
"""
def swap_list(l): 
    # l is the list for which the first and last elements will be swapped
    tmp = l[0]
    l[0]= l[len(l)-1] 
    l[len(l)-1] = tmp
    

l = [10, 9, 8, 1, 2, 3] # l points to list
a = l # a points to l

swap_list(a) # making changes to a makes changes to l and also the list

# l should be equal to [3, 9, 8, 1, 2, 10]

print(l)
