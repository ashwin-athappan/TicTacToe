board = [' ' for x in range(10)]


def printBoard(board):
    print('     |     |')
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}')
    print('     |     |')
    print('-----------------')
    print('     |     |')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}')
    print('     |     |')
    print('-----------------')
    print('     |     |')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}')
    print('     |     |')


def placeMarker(board, marker, pos):
    board[pos] = marker


def isSpaceFree(board, pos):
    return board[pos] == ' '


def win_check(board, marker):
    # 1  2  3
    # 4  5  6
    # 7  8  9

    return (board[1] == board[2] == board[3] == marker  # row 1
            or
            board[4] == board[5] == board[6] == marker  # row 2
            or
            board[7] == board[8] == board[9] == marker  # row 3
            or
            board[1] == board[4] == board[7] == marker  # col 1
            or
            board[2] == board[5] == board[8] == marker  # col 2
            or
            board[3] == board[6] == board[9] == marker  # col 3
            or
            board[1] == board[5] == board[9] == marker  # diagonal 1
            or
            board[7] == board[5] == board[3] == marker  # diagonal 2
            )


def isBoardFull(board):
    return board.count(' ') == 1


def playerMove():
    play = True
    while play:
        move = input('Enter the position you want to place the marker (1 - 9)')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if isSpaceFree(board, move):
                    play = False
                    placeMarker(board, 'X', move)
                else:
                    print('Space is not free')
            else:
                print('Out of range')
        except:
            print('Enter only numbers')


def comp_move():
    possibleMoves = [x for x, l in enumerate(board) if l == ' ' and x != 0]
    move = 0

    for i in [1, 3, 7, 9]:
        if board[i] == 'X':
            if isSpaceFree(board, 5):
                return 5

    for x in ['O', 'X']:
        for i in possibleMoves:
            board_copy = board.copy()
            board_copy[i] = x
            if win_check(board_copy, x):
                move = i
                return move

    cornersPossible = []

    for i in possibleMoves:
        if i in [1, 2, 3, 4, 6, 7, 8, 9]:
            cornersPossible.append(i)

    if len(cornersPossible) > 0:
        move = selectRandom(cornersPossible)
        return move

    if 5 in possibleMoves:
        return 5

    return move


def selectRandom(my_list):
    import random
    return random.choice(my_list)


def main():
    print('Welcome to TIC TAC TOE')
    choice = input('Do you want to start (Yes/No)')
    if choice.upper() == 'YES':
        while True:
            if not win_check(board, 'O'):
                playerMove()
                printBoard(board)
            else:
                print('Sorry the computer won')
                break

            if not win_check(board, 'X'):
                move = comp_move()
                if move == 0:
                    print('Tie Game!')
                else:
                    placeMarker(board, 'O', move)
                    print('Computer placed an \'O\' in position ', move, '.')
                    printBoard(board)
            else:
                print('Player Won!')
                break
        if isBoardFull(board):
            print('Tie Game!')


main()
