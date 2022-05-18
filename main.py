# Defining board 
board = [[' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' '],]

# Print board function
def printBoard():
    columnHeader = ''
    for i in range(7):
        columnHeader += '  ' + str(i+1) + ' '
    print(columnHeader)
    print('+---' *7 + '+')

    for row in range(len(board[0])):
        items=''
        for col in range(len(board)):
            items += '| ' + board[col][row] + ' '
        print(items + '|')
        print('+---' *7 + '+')
    print()

# Function to add a user defined piece
def addPiece(piece, column):
    print("Trying to place an " + piece.upper() + ' in column ' + str(column))
    error, msg = displayError(column)
    if error:
        print(msg)
        print()
        return False

    for row in range(len(board[0]), 0, -1):
        if board[column-1][row-1] == ' ':
            board[column-1][row-1] = piece.upper()
            break
        else:
            continue 
    print("Placed an " + piece + ' in column ' + str(column))
    print() 
    printBoard()

def displayError(column):
    msg=''
    if column > 7 or column < 1 or board[column-1][0] != ' ':
        msg = "Make sure to pick a column between 1 and 7 that is not full"
        return True, msg
    # elif piece.upper() not in 'XO':
    #   msg = "Make sure to use either 'X' or 'O' as your piece"
    #   return True, msg
    else: 
        return False, 'no err'

def detectWin(piece):
    # vertical
    for row in range(len(board[0])-3):
        for col in range(len(board)):
            if board[col][row] == board[col][row+1] == board[col][row+2] == board[col][row+3] == piece:
                return True

    # horizontal
    for row in range(len(board[0])):
        for col in range(len(board)-3):
            if board[col][row] == board[col+1][row] == board[col+2][row] == board[col+3][row] == piece:
                return True
    
    # diagonal \
    for row in range(len(board[0])-3):
        for col in range(len(board)-3):
            if board[col][row] == board[col+1][row+1] == board[col+2][row+2] == board[col+3][row+3] == piece:
                return True
        
    # diagonal /
    for row in range(len(board[0])):
        for col in range(len(board)-3):
            if board[col][row] == board[col+1][row-1] == board[col+2][row-2] == board[col+3][row-3] == piece:
                return True
    return False

def available_moves():
    # Returns the columns that are open
    moves = []
    for i in range(1, len(board)+1):
        error, msg = displayError(i)
        if not error:
            moves.append(i)
    return moves

def detectGameOver(piece):
    moves= available_moves()
    win = detectWin(piece)
    if win:
        return True
    elif len(moves) == 0:
        return True
    else: 
        return False

def play_game():
    printBoard()
    turn = 'X'

    while(not detectGameOver(turn)):
        col = 0
        available = available_moves()
        while (col not in available or col < 1 or col > 7):
            col = int(input("It is " + turn + "'s turn. Please choose a column. "))
            addPiece(turn, col)

        if detectWin(turn):
            print(turn + ' has won the game!')
            print()
            printBoard()
            break 

        if turn == 'X':
            turn = 'O'
        elif turn == 'O':
            turn = 'X'

        if len(available) == 0:
            print("It's a tie!")
            print()
            printBoard()
            break     

play_game()