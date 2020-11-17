"""
Tic Tac Toe Player
"""
import copy
import math

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
    if terminal(board):
        return None
    countX, countO = 0,0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                countX += 1
            if board[i][j] == O:
                countO += 1
    return O if countX > countO else X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    result = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                result.add((i,j))
    return result

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if terminal(board):
        raise ValueError("Game over!")
    elif action not in actions(board):
        raise ValueError("Cell occupied")
    else:
        p = player(board)
        result = copy.deepcopy(board)
        (i, j) = action
        result[i][j] = p
    return result

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != None:
            return board[i][0]

    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != None:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != None:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != None:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:
        return 1
    elif w == O:
        return -1
    return 0


def maxValue(board, alpha, beta):
    if terminal(board):
        return utility(board)

    max_value = -10000000
    for action in actions(board):
        max_value = max(max_value, minValue(result(board,action), alpha, beta))
        if max_value >= beta:
            break
        alpha = max(max_value, alpha)
    return max_value


def minValue(board, alpha, beta):
    if terminal(board):
        return utility(board)

    min_value = 10000000
    for action in actions(board):
        min_value = min(min_value, maxValue(result(board,action), alpha, beta))
        if min_value <= alpha:
            return min_value
        beta = min(min_value, beta)
    return min_value

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    pl = player(board)

    if pl == X:
        max_value = -10000000
        selected_action = None
        for action in actions(board):
            minValueResult = minValue(result(board, action), -10000000, 10000000)
            if minValueResult > max_value:
                max_value = minValueResult
                selected_action = action
    elif pl == O:
        min_value = 10000000
        selected_action = None
        for action in actions(board):
            maxValueResult = maxValue(result(board, action), -10000000, 10000000)
            if maxValueResult < min_value:
                min_value = maxValueResult
                selected_action = action
    return selected_action
