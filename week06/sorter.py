import myreadlines
import sys


def writetofile(lines, filename):
    # animals.txt
    # --> filename: animals 
    # --> file extension: txt
    # Assuming there is only one . in the filename

    filename, ext = filename.split('.')
    filename = "{}-sorted.{}".format(filename, ext)

    try:
        fp = open(filename, 'w') # 'w' to open in write mode
        i = 0
        while i < len(lines):
            fp.write("{}\n".format(lines[i]))
            i+=1 
    except Exception:
        raise Exception("An exception occurred while writing to file")
    finally:
        fp.close()




try:
    filename = sys.argv[1]
    lines = myreadlines.readlines(filename)
except IndexError as e:
    raise Exception("Filename was not passed to the program")

lines.sort()

writetofile(lines, filename)

