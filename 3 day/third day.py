def day3(square):

    rows = len(square)
    col = len(square[0])

    total = 0

    rowIndex = 0
    colIndex = 0

    while rowIndex < rows - 1:

        rowIndex += 1
        colIndex += 3

        if colIndex >= col:
            colIndex -= col

        row = square[rowIndex]
        spot = row[colIndex]

        if spot == '#':
            total += 1

    return total

with open("map.txt", "r") as inputFile:
    fileLines = inputFile.readlines()
    inputMap = [ list(line.strip()) for line in fileLines]
    #print(inputMap[:3])

print(day3(inputMap))