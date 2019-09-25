from strings import get_first_lowercase_pair

def test_simple_positive():
    test = "AAaaAA"
    assert get_first_lowercase_pair(test) == 2, "Error for {}".format(test)

    test = "xyz"
    assert get_first_lowercase_pair(test) == 0, "Error for {}".format(test)


def test_simple_negative():
    test = "ABC"
    assert get_first_lowercase_pair(test) == -1, "Error for {}".format(test)

    test = ""
    assert get_first_lowercase_pair(test) == -1, "Error for {}".format(test)


def test_edge_cases(): 
    test = 99
    assert get_first_lowercase_pair(test) == -1, "Error for {}".format(test)
    
    test = None
    assert get_first_lowercase_pair(test) == -1, "Error for {}".format(test)

test_simple_positive()
test_simple_negative()
test_edge_cases()
