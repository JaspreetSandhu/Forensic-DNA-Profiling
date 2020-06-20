import csv
from sys import argv, exit
from cs50 import get_string

def main(data, sequence):

    database = open(data, "r")

    reader = csv.reader(database)

    firstLine = next(reader)

    dnaDict = {}
    dnaNames = []

    for i in firstLine:
        #if i != 'name':
         #   dnaDict[i] = 0

        dnaDict[i] = 0
        dnaNames.append(i)


    for dnaStr in dnaDict:
        dnaDict[dnaStr] = dnaCount(dnaStr)

    name = ''

    for row in reader:

        length = len(row)

        dataList = []
        dnaList = []

        for i in range(1, length):

            dataList.append(int(row[i]))
            dnaList.append(dnaDict[dnaNames[i]])

        if dataList == dnaList:
            name = row[0]


    database.close()

    if name != '':
        print(name)
    else:
        print("No Match.")

    return



def dnaCount(name):

    count = 0

    count = line.count(name)

    return count


if len(argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit(1)

tmp = open(argv[2], "r")
line = tmp.read()


main(argv[1], line)
exit(0)

