num = input()
num = int(num)

if (num % 2 == 0) and (num >= 20 and num <= 200):
    print("{} is even and in the range [20,200]".format(num))
elif (num % 2 == 1) and (num < 0):
    print("{} is odd and negative".format(num))
else:
    print("Neither conditions were met")
