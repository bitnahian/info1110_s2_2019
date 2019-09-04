"""
Function that emulates Python's zip function
"""
def my_zip(ls_1, ls_2):
    if type(ls_1) != list or len(ls_1) < 1:
        print("Wrong parameter type")
        return

    if type(ls_2) != list or len(ls_2) < 1:
        print("Wrong parameter type")
        return

    len_ls_1 = len(ls_1)
    len_ls_2 = len(ls_2)
    
    # Find the minimum length
    min_len = min(len_ls_1, len_ls_2)

    ret_lst = []
    i = 0
    while i < min_len:
        ret_lst.append((ls_1[i], ls_2[i]))
        i += 1

    return ret_lst

a_spam = ['a', 'b', 'c', 'd']
b_spam = ['W', 'X', 'Y', 'Z']

z_spam = my_zip(a_spam, b_spam) # [('a', 'W'), ('b', 'X'), ('c', 'Y'), ('d', 'Z')]

print(z_spam)

assert z_spam == [('a', 'W'), ('b', 'X'), ('c', 'Y'), ('d', 'Z')], "z_spam error"


names = ['Alice', 'Bob', 'Carol']
ages = [32, 51, 15, 5, 25, 48] # list `ages` is longer than list `names`
zipped = my_zip(names, ages) # [('Alice', 32), ('Bob', 51), ('Carol', 15)]

print(zipped)

assert zipped == [('Alice', 32), ('Bob', 51), ('Carol', 15)], "zipped error"

