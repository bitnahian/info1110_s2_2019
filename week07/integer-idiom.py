def integer(str_val):
    """
    Converts str_val to integer
    """
    if not str_val.isdigit():
        raise ValueError("String is not a number")

    digits = list(str_val)
    i = 0
    num = 0
    while i < len(digits):
        base = 10 ** (len(digits) - 1 - i)
        num += convert_to_int(digits[i]) * base
        i += 1
    
    return num

def convert_to_int(ch):
    if ch == '0':
        return 0
    elif ch == '1':
        return 1
    elif ch == '2':
        return 2
    elif ch == '3':
        return 3
    elif ch == '4':
        return 4
    elif ch == '5':
        return 5
    elif ch == '6':
        return 6
    elif ch == '7':
        return 7
    elif ch == '8':
        return 8
    elif ch == '9':
        return 9

assert integer('4321') == 4321, 'Function didn\'t work'  # -> 4 * 1000 + 3 * 100 + 2 * 10 + 1 * 1
assert integer('123456') == 123456, 'Function didn\'t work'
