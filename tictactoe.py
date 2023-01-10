"""
Tic Tac Toe Player
"""
import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    total = 0
    # if an X is in the board, add 1 to total
    # if an O is in the board, subtract 1 from total
    for row in range(3):
        for column in range(3):
            if board[row][column] == X:
                total += 1
            elif board[row][column] == O:
                total += -1
    
    # current player = O if amount of X's >= amount of O's
    if total >= 0:
        return O
    # current player = X if amount of O's > amount of X's
    else:
        return X
    #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    list = []
    # if spot in board is empty, add tuple to list
    for row in range(3):
        for column in range(3):
            if board[row][column] == None:
                list.append((row, column))

    return list

    #raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = copy.deepcopy(board)
    #newBoard = board

    newBoard[action[0]][action[1]] = player(board)

    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # if a single row is filled with X/O, return X/O
    for row in board:
        if row[0] == row[1] == row[2] != None:
            if row[0] == X:
                return X
            else:
                return O

    # if a single column is filled with X/O, return X/O
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] != None:
            if board[0][column] == X:
                return X
            else:
                return O

    # if the diagonal (topleft -> bottomright) is filled with X/O, return X/O
    if board[0][0] == board[1][1] == board[2][2] != None:
        if board[0][0] == X:
            return X
        else:
            return O

    # if the diagonal (topright -> bottomleft) is filled with X/O, return X/O
    if board[0][2] == board[1][1] == board[2][0] != None:
        if board[0][2] == X:
            return X
        else:
            return O

    # else, return None; no winner yet
    return None

    #raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # if board has a winning player, return True
    win = winner(board)
    if win != None:
        return True

    # if entire board is filled, return True
    filled = 0
    for row in range(3):
        for column in range(3):
            if board[row][column] != None:
                filled += 1
    if filled == 9:
        return True

    # else, return False; game is not over
    return False

    #raise NotImplementedError


def score(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # checkwinner = X, O, or None
    checkwinner = winner(board)

    if checkwinner == X:
        return 1
    elif checkwinner == O:
        return -1
    else:
        return 0

    #raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def min_value(board):
        if terminal(board):
            return score(board)
        v = math.inf
        for action in actions(board):
            value = max_value(result(board, action))
            if value < v:
                v = value
        return v


    def max_value(board):
        if terminal(board):
            return score(board)
        v = -math.inf
        for action in actions(board):
            value = min_value(result(board, action))
            if value > v:
                v = value
        return v


    opt_act = None

    if terminal(board):
        return None
    
    if player(board) == X:
        inf = -math.inf
        for action in actions(board):
            value = min_value(result(board, action))
            if value > inf:
                inf = value
                opt_act = action

    elif player(board) == O:
        inf = math.inf
        for action in actions(board):
            value = max_value(result(board, action))
            if value < inf:
                inf = value
                opt_act = action
    return opt_act