a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))
e = int(input("Enter e: "))

nums = [a, b, c, d, e]

# Set up your counter
i = 0

sum_val = 0

while i < len(nums): # Standard idiom for looping over a list
    # Do something
    if nums[i] == 7:
        i += 2
        continue 
    sum_val += nums[i]
    i+=1


