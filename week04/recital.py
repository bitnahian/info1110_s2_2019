# Write a program recital.py that reads numbers from standard input. When the user enters zero, the program recites all the numbers entered (excluding the zero).

user_inputs = [] # Create empty list

while True:
    user_input = input("Enter a number: ")
    if user_input == "0":
        # If user enters 0, break from loop
        break
    user_inputs.append(user_input) # Append to list

print("Your numbers were: ")

i = 0 # Create your counter

while i < len(user_inputs):
    print(user_inputs[i])
    i+=1

