import random

print("Welcome to Connect Four")
print("-----------------------")

possibleLetters = ["A", "B", "C", "D", "E", "F", "G"]
gameBoard = [["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""]]

rows = 6
cols = 7

def printGameBoard():
    print("\n     A    B    C    D    E    F    G  ", end="")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+")
        print(x, " |", end="")
        for y in range(cols):
            if gameBoard[x][y] == "🔵" or gameBoard[x][y] == "🔴":
                print("", gameBoard[x][y], end=" |")
            else:
                print(" ", gameBoard[x][y], end="  |")
    print("\n   +----+----+----+----+----+----+----+")

def modifyArray(spacePicked, turn):
    gameBoard[spacePicked[0]][spacePicked[1]] = turn

def checkForWinner(chip):
    # Check horizontal spaces
    for y in range(rows):
        for x in range(cols - 3):
            if gameBoard[y][x] == chip and gameBoard[y][x+1] == chip and gameBoard[y][x+2] == chip and gameBoard[y][x+3] == chip:
                print("\nGame Over!", chip, "wins! Thank you for playing :)")
                return True

    # Check vertical spaces
    for x in range(cols):
        for y in range(rows - 3):
            if gameBoard[y][x] == chip and gameBoard[y+1][x] == chip and gameBoard[y+2][x] == chip and gameBoard[y+3][x] == chip:
                print("\nGame Over!", chip, "wins! Thank you for playing :)")
                return True

    # Check diagonal (top right to bottom left) spaces
    for y in range(rows - 3):
        for x in range(3, cols):
            if gameBoard[y][x] == chip and gameBoard[y+1][x-1] == chip and gameBoard[y+2][x-2] == chip and gameBoard[y+3][x-3] == chip:
                print("\nGame Over!", chip, "wins! Thank you for playing :)")
                return True

    # Check diagonal (top left to bottom right) spaces
    for y in range(rows - 3):
        for x in range(cols - 3):
            if gameBoard[y][x] == chip and gameBoard[y+1][x+1] == chip and gameBoard[y+2][x+2] == chip and gameBoard[y+3][x+3] == chip:
                print("\nGame Over!", chip, "wins! Thank you for playing :)")
                return True

    return False

def coordinateParser(inputString):
    coordinate = [None] * 2
    if inputString[0] in possibleLetters:
        coordinate[1] = possibleLetters.index(inputString[0])
    else:
        print("Invalid column")
    coordinate[0] = int(inputString[1])
    return coordinate

def isSpaceAvailable(intendedCoordinate):
    if gameBoard[intendedCoordinate[0]][intendedCoordinate[1]] == '🔴' or gameBoard[intendedCoordinate[0]][intendedCoordinate[1]] == '🔵':
        return False
    return True

def gravityChecker(intendedCoordinate):
    spaceBelow = [intendedCoordinate[0] + 1, intendedCoordinate[1]]
    if intendedCoordinate[0] == rows - 1:  # Ground level
        return True
    if not isSpaceAvailable(spaceBelow):  # There's a piece below
        return True
    return False

turnCounter = 0
while True:
    if turnCounter % 2 == 0:  # Player turn
        printGameBoard()
        while True:
            spacePicked = input("\nChoose a space (e.g., A5): ")
            coordinate = coordinateParser(spacePicked)
            try:
                if isSpaceAvailable(coordinate) and gravityChecker(coordinate):
                    modifyArray(coordinate, '🔵')
                    break
                else:
                    print("Not a valid coordinate")
            except:
                print("Error occurred, please try again")
        winner = checkForWinner('🔵')
        turnCounter += 1
    else:  # Computer turn
        while True:
            column = random.choice(possibleLetters)
            for row in reversed(range(rows)):  # Start from the bottom row
                cpuCoordinate = [row, possibleLetters.index(column)]
                if isSpaceAvailable(cpuCoordinate):
                    modifyArray(cpuCoordinate, '🔴')
                    break
            else:
                continue  # If the column is full, choose another one
            break
        print("\nComputer chose column", column)
        winner = checkForWinner('🔴')
        turnCounter += 1

    if winner:
        printGameBoard()
        break
