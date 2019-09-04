"""
Function that takes in a list and mimics Python's enumerate function and returns a list of tuples with each tuple containing the (index, element) of each element in ls
"""
def my_enum(ls):
    
    if type(ls) != list or len(ls) < 1:
        print("Wrong parameter type or list is empty")
        return

    ret_list = []
    i = 0 
    while i < len(ls):
        ret_list.append((i, ls[i]))
        i+=1

    return ret_list


spam = ['a', 'b', 'c', 'd', 'e']
e_spam = my_enum(spam) # [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]

assert (e_spam == [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]), "e_spam error"


ham = [True]
e_ham = my_enum(ham) # [(0, True)]

assert (e_ham == [(0, True)]), "e_ham error"

eggs = []
e_eggs = my_enum(eggs) # []

assert (e_eggs == None), "e_eggs error"
