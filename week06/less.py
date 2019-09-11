import sys 
import os

try:
    filename = sys.argv[1]
    if not os.path.exists(filename):
        raise ValueError("File does not exist in directory")
except IndexError as e:
    raise Exception("Filename was not passed to the program")
except ValueError as e:
    raise Exception(e)



try:
    mode = 'r' # 'w', 'a'
    fp = open(filename, mode)

    # Do whatever you need to do with the file after opening and before closing it
    while True:
        line = fp.readline()
        if line == "":
            # This means that EOF has been reached
            break
        line = line.rstrip("\n")
        # Strip away the "\n" at the end of the string
        usr_input = input()
        if usr_input == "":
            print(line)
        elif usr_input == "q":
            break

    # How would I read all the lines WITHOUT using fp.readlines()
except Exception:
    print("An exception ocurred while reading the file")
finally:
    fp.close() # Put your close statement inside a finally block
