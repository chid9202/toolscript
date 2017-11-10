import os
import re
# return line number in the filename with the matching pattern string
def search(filename, pat):
    lineNumbers = []
    with open(filename) as myFile:
        for num, line in enumerate(myFile, 1):
            if pat in line:
                lineNumbers.append(num)
    if not lineNumbers:
        return False
    return lineNumbers
def find(op1):
    # Collect file names with the entire path
    filenames = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            s = str(root + '/' + file)
            filenames.append(s)
    pattern = op1
    # Search the pattern from the files and read the line
    for file in filenames:
        result = search(file, pattern)
        if result == False:
            continue
        fo = open(file, "r")
        lines = fo.readlines()
        print("File name: " + fo.name)
        for lineNumb in result:
            new = re.sub('^\s+', "", lines[lineNumb-1]) # remove spaces at the beginning of each line
            print("Line" , lineNumb , ":" , new , end='')
        print()
        fo.close()

def main():
    command = ""
    while command != "quit":
        # Initialize variables every time
        commandLine = ""
        command = ""
        op1 = ""
        op2 = ""
        commandLine = input("$")
        # Determine number of operators
        if len(commandLine.split()) == 1:
            command = commandLine.split()[0]
        elif len(commandLine.split()) == 2:
            command = commandLine.split()[0]
            op1 = commandLine.split()[1]
        elif len(commandLine.split()) == 3:
            command = commandLine.split()[0]
            op1 = commandLine.split()[1]
            op2 = commandLine.split()[2]
        else:
            print("too manny operators")

        # Dtermine which command
        if command == "find":
            find(op1)
        # TODO: More commands
        # TODO: Convert units
        elif command == "convert":
            print()
        # List commands
        elif command == "?":
            print("find op1")
            print("convert op1(unit of op2) op2")
            print("?")
        else:
            print()

if __name__ == "__main__":
    main()
