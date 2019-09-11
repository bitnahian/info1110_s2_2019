import sys
import os

def readlines(filename):
    try:
        if not os.path.exists(filename):
            raise ValueError("File does not exist in directory")
    except IndexError as e:
        raise Exception("Filename was not passed to the program")
    except ValueError as e:
        raise Exception(e)
    
    lines = [] # Initialise your list

    try:
        mode = 'r' # 'w', 'a'
        fp = open(filename, mode)

        # Do whatever you need to do with the file after opening and before closing it
        while True:
            line = fp.readline()
            if line == "":
                # This means that EOF has been reached
                break
            line = line.strip() # Strip the line off all whitespaces
            lines.append(line)

        # How would I read all the lines WITHOUT using fp.readlines()
    except Exception:
        print("An exception ocurred while reading the file")
    finally:
        fp.close() # Put your close statement inside a finally block

    return lines



# print(readlines(sys.argv[1]))
