while True:  
    num = input("Integer: ")
    num = int(num)
    
    num_is_even = (num % 2 == 0)
    num_is_in_range = (num >= 20 and num <= 200)

    num_is_odd = (num % 2 == 1)
    num_is_neg = (num < 0)

    if num_is_even and num_is_in_range:
        print("{} is even and in the range [20,200]".format(num))
    elif num_is_odd and num_is_neg:
        print("{} is odd and negative".format(num))
    elif num == 0:
        break
    else:
        print("Neither conditions were met")
