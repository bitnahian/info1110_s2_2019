"""
Basic idioms for python learning
"""
import time


def check_error(ls):
    if not isinstance(ls, list):
        raise TypeError("ls is not of type list")
    i = 0
    while i < len(ls):
        if not isinstance(ls[i], str):
            raise TypeError("{}-th element of ls is not string".format(i))
        i+=1
    
"""
A function longest(words) , which takes a list of strings words and returns the longest string. If there are two strings of the same length that fit this criteria, return the last one found. If words is empty, return None .
"""
def longest(ls):

    # Check for errors
    check_error(ls)    
    
    # Check if length is equals 0, ls -> []
    if len(ls) == 0:
        return None
    
    # Basic idiom to find the maximum component in a list

    # The idea is to assume that the longest word is the first word in the list
    # and look at every other word sequentially

    max_len = len(ls[0])
    max_word = ls[0]

    i = 0
    while i < len(ls):
        if len(ls[i]) >= max_len:
            time.sleep(1)
            max_word = ls[i]
            max_len = len(ls[i])
        i+=1

    return max_word



def longest_v2(ls):

    # Check for errors
    check_error(ls)    
    
    # Check if length is equals 0, ls -> []
    if len(ls) == 0:
        return None
    
    # Basic idiom to find the maximum component in a list

    # The idea is to assume that the longest word is the first word in the list
    # and look at every other word sequentially

    max_len = len(ls[-1]) # You can index using -1 to find the last element
    max_word = ls[-1]

    i = len(ls) - 1
    while i >= 0:
        if len(ls[i]) > max_len:
            time.sleep(1)
            max_word = ls[i]
            max_len = len(ls[i])
        i -= 1

    return max_word


def shortest(ls):
    # Check for errors
    check_error(ls)    
    
    # Check if length is equals 0, ls -> []
    if len(ls) == 0:
        return None
    
    min_len = len(ls[0])
    min_word = ls[0]

    i = 0
    while i < len(ls):
        if len(ls[i]) < min_len:
            min_word = ls[i]
            min_len = len(ls[i])
        i+=1
    return min_word


def av_len(ls):
    pass

def start_count(ls, ch):
    # Check for errors
    check_error(ls)    
    
    # Check if length is equals 0, ls -> []
    if len(ls) == 0:
        return None
    # Objective - find the number of strings s in words starting with the letter ch .
    num_strings = 0

    i = 0
    while i < len(ls):
        if ls[i].startswith(ch):
            num_strings += 1
        i+=1
    return num_strings

dogs = ['Collie', 'Retriever', 'Corgi', 'Labrador', 'Husky', 'Malamute', 'aaaaaaaaaa', 'bbbbbbbbbb', 'cccccccccc']

#assert longest(dogs) == 'cccccccccc', "Error in function longest"
assert longest_v2(dogs) == 'cccccccccc', "Error in function longest"
#assert shortest(dogs) == 'Corgi', 'Error in function shortest'
#assert av_len(dogs) == sum([len(i) for i in dogs])/len(dogs) , 'Error in funciton av_len'
assert start_count(dogs, 'C') == 2, 'Error in function start_count'
