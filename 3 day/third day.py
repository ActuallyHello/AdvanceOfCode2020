def day3(square, indR, indC):

    rows = len(square)
    col = len(square[0])

    total = 0

    rowIndex = 0
    colIndex = 0

    while rowIndex < rows - 1:

        rowIndex += indR
        colIndex += indC

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

print("part 1 -> ",day3(inputMap, 1, 3))
print("part 2 -> ",day3(inputMap, 1,1) * day3(inputMap, 1,3) * day3(inputMap, 1,5) * day3(inputMap, 1,7) * day3(inputMap, 2,1))