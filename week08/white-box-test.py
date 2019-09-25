from white_box import my_max

assert my_max([0, 1, 1]) == 1, "Error"

assert my_max([]) == -1, "Output for empty list should be -1"

assert my_max("abc") == -1, "Output for different data type should be -1"

assert my_max(["1", 2, 3]) == -1, "Function should return -1 if all elements are not numbers"

assert my_max([1, 99, 3]) == 1, "Function should be returning index of largest number"

assert my_max([1, 2, 5, 5, 1]) == 2, "Function should be returning first index"

assert my_max([1, 2, 99]) == 2, "Function should check the last index"
