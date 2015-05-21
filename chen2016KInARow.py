'''chen2016KlnARow.py
CSE 415 HW5
May 6th 2015
This python contains methods for players to make a clear move by
foresee furture steps and the winner has k elements in same column
, row, or diagonal line.
Finished by group of Yinghe Chen, and Yu Fu
'''

from random import randint
from copy import deepcopy
import time

def prepare(initial_state, k, what_side_I_play, opponent_nickname):
    '''Take four arguments and remeber these values for the game.'''
    global initial_state_input
    global initial_row
    global initial_col
    global self_side
    global oppo_side
    global oppo_name
    global k_size

    initial_state_input = initial_state
    k_size = k
    self_side = what_side_I_play
    oppo_name = opponent_nickname

    if self_side == 'X':
        oppo_side = 'O'
    elif self_side == 'O':
        oppo_side = 'X'
    else:
        return "Error: Invalid input of what_side_I_play"

    initial_row = len(initial_state_input[0])
    initial_col = len(initial_state_input[0][0])

    S = initial_row * initial_col
    P = 4
    myint(S, P)

    return "OK"

def myint(S, P):
    '''Set up a S by P array of random integers.'''
    global zobristnum
    zobristnum = [[0 for i in range(P)] for j in range(S)]

    for i in range(S):
        for j in range(P):
            zobristnum[i][j] = randint(0, 4294967296)

def zhash(board, S):
    '''Hash the given board state to an integer'''
    global zobristnum
    val = 0
    for i in range(S):
        piece = None
        if (board[i] == ' '): piece = 0
        if (board[i] == 'X'): piece = 1
        if (board[i] == 'O'): piece = 2
        if (board[i] == '-'): piece = 3
        if (piece != None): val ^= zobristnum[i][piece]
        return val

def introduce():
    '''Introcuce the player, giving the agent's full name, and name of creators'''
    return "Hey My dear opponent! My name is chen2016KInArow, developed by YC and YF.\
            I am the master of K-in-Row. Let me beat you!"

def nickname():
    '''Return a short version of the playing agent's name'''
    return "WHATEVER"

def makeMove(currentState, currentRemark, timeLimit = 10000):
    '''Use miniMax search to determine next move in the game.'''
    MIN = -100000
    MAX = 100000
    plyLeft = 3
    time_start = time.time()
    (moveEval, moveState) = miniMax(currentState, plyLeft, MIN, MAX, time_start, timeLimit)
    list = ["I have foresee your move!", "That is what I thought!", "I know you will do it",
            "Haha, I am winning!", "What a big move you did!", "You are never going to beat me!",
            "you are killing yourself!", "That is a bad idea!", "Bad"]
    randNum = randint(0, len(list)-1)
    newRemark = list[randNum]
    move = get_move(currentState, moveState)
    return [[move, moveState], newRemark]

def get_move(state1, state2):
    ''' Return the [row, col] as the moving opration between two states.'''
    board1 = state1[0]
    board2 = state2[0]
    for i in range(len(board1)):
        for j in range(len(board1[i])):
            if board1[i][j] != board2[i][j]:
                return [i, j]

def miniMax(state, plyLeft, MIN, MAX, time_start, timeLimit):
    '''Recursive miniMax search to search for plyLeft levels,
       return the state most likely lead to win.'''
    if time.time() - time_start > timeLimit * 0.8:
        return (staticEval(state), state)
    ss = sucessors(state)
    if plyLeft == 0 or ss == []:
        return (staticEval(state), state)
    board = state[0]
    side = state[1]

    if side == 'X':
        dynamicMin = MIN
        stateToReturn = state
        for i in range(len(ss)):
            (nextEval, nextState) = miniMax(ss[i], plyLeft - 1, dynamicMin, MAX, time_start, timeLimit)
            if nextEval > dynamicMin:
                dynamicMin = nextEval
                stateToReturn = ss[i]
        return (staticEval(stateToReturn), stateToReturn)

    else:
        dynamicMax = MAX
        stateToReturn = state
        for i in range(len(ss)):
            (nextEval, nextState) = miniMax(ss[i], plyLeft - 1, MIN, dynamicMax, time_start, timeLimit)
            if nextEval < dynamicMax:
                dynamicMax = nextEval
                stateToReturn = ss[i]
        return (staticEval(stateToReturn), stateToReturn)

def sucessors(state):
    '''Return all the sucessors of given state.'''
    board = state[0]
    side = state[1]
    ss = []            # list of all the sucessors
    for i in range(initial_row):
        for j in range(initial_col):
            if board[i][j] == ' ':
                sucessor = deepcopy(board)
                sucessor[i][j] = side
                ss.append([sucessor, switch_side(side)])
    return ss

def switch_side(side):
    if side == 'X':
        return 'O'
    elif side == 'O':
        return 'X'
    else:
        return ''

def staticEval(state):
    '''Return a static evaluation of the given state. High if good for X. Low if good for O.'''
    board = state[0]
    return staticEvalHelper(board, 'X') - staticEvalHelper(board, 'O')

def staticEvalHelper(board, side_mark):
    '''For the given board, for each segment with size k in rows, columns and diagonals,
       if the segment contains only the side_mark, count number of side_mark.
       Add 10 ^ (number of side_mark - 1) to evaluation score.'''
    # For example, k_size = 4, MAX = 1000
    # If there are 4 O's in the segment, the score is 1000 (MAX)
    #              3 O's in the segment, the score is 100
    #              2 O's in the segment, the score is 10
    #              1 O's in the segment, the score is 1
    score = 0
    # rcd means row/column/diagonal
    rcds = get_rows(board) + get_cols(board) + get_forward_diagonals(board) + get_backward_diagonals(board)
    segments = []
    for rcd in rcds:
        if len(rcd) >= k_size:
            for i in range(len(rcd) - k_size + 1):
                segment = rcd[i : i + k_size]
                segments.append(segment)
    for segment in segments:
        count = 0
        for cell in segment:
            if cell == side_mark:
                count += 1
            elif cell != ' ':
                count = 0
                break
        if count > 0:
            score += 10 ** (count - 1)
    return score

def get_rows(board):
    '''Return a list of rows in the given board.'''
    return [[cell for cell in row] for row in board]

def get_cols(board):
    '''Return a list of columns=s in the given board.'''
    cols = [[] for col in board[0]]
    for row in board:
        for col_index, cell in enumerate(row):
            cols[col_index].append(cell)
    return cols

def get_forward_diagonals(board):
    '''Return a list of forward diagonal elements list in the given board.'''
    buff = ['B']*(len(board[0])+1)
    buff_grid = []
    for row_index, row in enumerate(get_rows(board)):
        buff_grid.append( buff[row_index:] + row + buff[:row_index+1] )
    cols = get_cols(buff_grid)[2:-1]
    for col in cols:
        while 'B' in col:
            col.remove('B')
    return cols

def get_backward_diagonals(board):
    '''Return a list of backward diagonal elements list in the given board.'''
    buff = ['X']*(len(board[0])+1)
    buff_grid = []
    for row_index, row in enumerate(get_rows(board)):
        buff_grid.append( buff[:row_index+1] + row + buff[row_index:] )
    cols = get_cols(buff_grid)[1:-2]
    for col in cols:
        while 'X' in col:
            col.remove('X')
    return cols

def testprint(l):
    for ll in l:
        print(ll)


#board = [["-", " ", " ", " ", "-"],\
#         [" ", " ", "X", "O", " "],\
#         [" ", " ", "O", "X", " "],\
#         [" ", " ", "O", " ", "X"],\
#         ["-", " ", " ", " ", "-"]]
#state = [board, 'O']
#print("row")
#testprint(get_rows(board))

#prepare(state, 4, 'O', 'hehe')
#print("col")
#testprint(get_cols(board))

#print("backward dia")
#testprint(get_backward_diagonals(board))

#print("forward dia")
#testprint(get_forward_diagonals(board))

#print(sucessors(state))
#print(staticEval(state))
#print(makeMove(state, 0, 1000))

