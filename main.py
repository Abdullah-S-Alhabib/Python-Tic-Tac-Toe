import random as rd

# This list contains all board values as matrix

board = [[0, '1', '2', '3'], [1, '-', '-', '-'], [2, '-', '-', '-'], [3, '-', '-', '-']]

row = 0

col = 0

# Turn tracker

turnNumb = 0

# variables for whether player and computer play X or O.

player = ''

computer = ''

takenSpace = []

possibleSpace = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]


def printSquares():
    """

    Prints the board to the output.

    :return: N/A

    """

    for i in board:
        print(i)


printSquares()

# player = 1, Computer = 2

turn = 1


def getRow():
    """

    Gets input from user for the row number, put the input in the *row* global variable.

    :return: N/A

    """

    global row

    row = int(input('Row number:'))

    if row == 0 or row > 3:
        print('Row cannot be 0 or larger than 3, please re enter')

        getRow()


def getCol():
    """

    Gets input from user for the row number, put the input in the *col* global variable.

    :return: N/A

    """

    global col

    col = int(input('Column number:'))

    if col == 0 or col > 3:
        print('Column cannot be 0 or larger than 3, please re enter')

        getCol()


def checkBoard():
    """

    Check for win conditions.

    :return: N/A

    """

    global takenSpace

    if len(takenSpace) == 9:
        print('Board is full, it\'s a draw!')

        exit()

    # Check for row win

    checker = checkRowWin()

    if checker == 'X':

        print('X won!')

        exit()

    elif checker == 'O':

        print('O won!')

        exit()

    # check for column win

    checker = checkColWin()

    if checker == 'X':

        print('X won!')

        exit()

    elif checker == 'O':

        print('O won!')

        exit()

    checkDiagonalWin()

    if checker == 'X':

        print('X won!')

        exit()

    elif checker == 'O':

        print('O won!')

        exit()


def checkDiagonalWin():
    """

    Check the diagonals for win conditions

    :return: 'X' if x won, 'O' if o won, 'none' if neither won.

    :return: 'lxi' when x is close to winning from the left to right diagonal, or 'loi' if it's o instead,

     i is the spot number in the diagonal

    :return: 'rxi' when x is close to winning from the right to left diagonal, or 'roi' if it's o instead

    """

    # check for left to right diagonal

    checker = ''

    temp = 0

    tempDiag = ''

    for i in range(1, 4):

        if board[i][i] == '-':
            temp = i

        checker += board[i][i]

    if checker == 'XXX':
        return 'X'

    if checker == 'OOO':
        return 'O'

    if checker in ['XX-', 'X-X', '-XX']:
        tempDiag = 'lx' + str(temp)

    if checker in ['OO-', 'O-O', '-OO']:
        tempDiag = 'lo' + str(temp)

    # check for right to left diagonal

    checker = ''

    j = 4

    for i in range(1, 4):

        j -= 1

        if board[i][i] == '-':
            temp = i

        checker += board[i][j]

    if checker == 'XXX':
        return 'X'

    if checker == 'OOO':
        return 'O'

    if checker in ['XX-', 'X-X', '-XX']:
        tempDiag = 'rx' + str(temp)

    if checker in ['OO-', 'O-O', '-OO']:
        tempDiag = 'ro' + str(temp)

    if bool(tempDiag):
        print(tempDiag)

        return tempDiag


def checkColWin():
    """

    Check the column for win conditions

    :return: 'X' if x won, 'O' if o won, 'none' if neither won.

    :return: i if x/o is close to winning,  where i is the number of the column

    """

    checker = ''

    tempCol = 0

    for i in range(1, 4):

        for j in range(1, 4):
            checker += board[j][i]

        if checker == 'XXX':

            return 'X'

        elif checker == 'OOO':

            return 'O'

        if checker in ['XX-', 'X-X', '-XX', 'OO-', 'O-O', '-OO']:
            tempCol = i

        checker = ''

    if bool(tempCol):
        return tempCol

    return 'none'


def checkRowWin():
    """

    Check the column for win conditions

    :return: 'X' if x won, 'O' if o won, 'none' if neither won.

    :return: 'xj' if x is close to winning, 'oj' if o is close to winning, where j is the number of the column

    """

    checker = ''

    tempRow = 0

    for i in range(1, 4):

        for j in range(1, 4):
            checker += board[i][j]

        if checker == 'XXX':

            return 'X'

        elif checker == 'OOO':

            return 'O'

        if checker in ['XX-', 'X-X', '-XX', 'OO-', 'O-O', '-OO']:
            tempRow = i

        checker = ''

    if bool(tempRow):
        return tempRow

    return 'none'


def computerPlay():
    global possibleSpace

    """

    Computer function, this handles the computer's turn.

    :return: N/A

    """

    global takenSpace, row, col, board, possibleSpace

    # Take the middle spot if it's not taken early in the game.

    row1 = 2

    col1 = 2

    if [row1, col1] not in takenSpace and turnNumb < 3:
        row = row1

        col = col1

        # assign X/O to the specified spot.

        board[row][col] = computer

        # assign the space as taken.

        takenSpace.append([row, col])

        possibleSpace.remove([row, col])

        return

    # check for winning spots for either player or computer, take the remaining spot.

    # check the columns:

    checker = checkColWin()

    if type(checker) == int:

        for i in range(1, 4):

            if board[i][checker] == '-':
                board[i][checker] = computer

                takenSpace.append([i, checker])

                possibleSpace.remove([i, checker])

                return

    # check the rows:

    checker = checkRowWin()

    if type(checker) == int:

        for i in range(1, 4):

            if board[checker][i] == '-':
                board[checker][i] = computer

                takenSpace.append([checker, i])

                possibleSpace.remove([checker, i])

                return

    # check diagonals:

    checker = checkDiagonalWin()

    if type(checker) == str and len(checker) > 1:

        temp = int(checker[2])

        if checker[0] == 'l':

            board[temp][temp] = computer

            takenSpace.append([temp, temp])

            possibleSpace.remove([temp, temp])

            return

        elif checker[0] == 'r':

            if temp == 1:

                board[1][3] = computer

                takenSpace.append([1, 3])

                possibleSpace.remove([1, 3])

                return

            elif temp == 3:

                board[3][1] = computer

                takenSpace.append([3, 1])

                possibleSpace.remove([3, 1])

                return

    # if no one is close to winning, pick a spot randomly:

    rand = rd.choice(possibleSpace)

    row = rand[0]

    col = rand[1]

    if rand in takenSpace:

        print('random generation error, rand generated taken space')

    else:

        board[row][col] = computer

        takenSpace.append([row, col])

        possibleSpace.remove([row, col])

        return


def checkSpace(row1, col1):  # args named row1 and col1 so as to not shadow the global variable names.

    """

    checks the specified spot for occupancy

    :param row1: Row number

    :param col1: Column number

    :return: If the spot is taken return 1 otherwise return 0.

    """

    global takenSpace

    checker = [row1, col1]

    if checker in takenSpace:
        return 1

    return 0


def getPlayer():
    """

    Take input to determine which letter the player is taking, then give the computer the other one.

    :return: N/A

    """

    global player, computer

    temp = int(input('Choose X or O, Please enter 1 for X, 2 for O:'))

    if temp == 1:

        player = 'X'

        computer = 'O'

    elif temp == 2:

        player = 'O'

        computer = 'X'

    else:

        print('Input is wrong, please re-enter:')

        getPlayer()


def main():
    global board, row, col, turn, takenSpace, turnNumb, player, computer, possibleSpace

    getPlayer()

    print(

        'First turn is the player, choose the index of where you want to place your ' + player + 'by entering the row '

                                                                                                 'number and '

                                                                                                 'column number')

    while 1:

        checkBoard()

        if turn == 1:

            print('It is ' + player + ' turn, enter the row and column numbers as prompted:')

            getRow()

            getCol()

            if checkSpace(row, col) == 0:

                # assign x/o to the specified spot.

                board[row][col] = player

                # assign the space as taken.

                takenSpace.append([row, col])

                possibleSpace.remove([row, col])

                # change player turn.

                turn = 2

                # print the board again.

                printSquares()

            else:

                print('The space you entered is taken, please enter another space')

        checkBoard()

        if turn == 2:
            print('It is now the computer\'s turn:')

            computerPlay()

            turn = 1

            turnNumb += 1

            printSquares()


main()
