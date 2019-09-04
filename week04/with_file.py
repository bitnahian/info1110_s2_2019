import sys

if len(sys.argv) < 2:
    # Error checking
    print("File name not provided")
    sys.exit(1)

filename = sys.argv[1]
mode = 'r'

with open(filename, mode) as fp:

    # Do whatever you need to do with the file after opening and before closing it
    lines = []
    while True:
        line = fp.readline()
        if line == "": 
            # This means that EOF has been reached
            break
        line = line.rstrip("\n") 
        # Strip away the "\n" at the end of the string
        lines.append(line)
        print(line)

# How would I read all the lines WITHOUT using fp.readlines()


