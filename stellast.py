from copy import deepcopy 
from re import sub
from random import choice
import time

initial = [[['-',' ',' ',' ',' ',' ','-'],
                [' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' '],
                ['-',' ',' ',' ',' ',' ','-']], "X"]

test =        [[['-',' ',' ',' ',' ',' ','-'],
                [' ','O',' ',' ',' ',' ',' '],
                [' ',' ','O',' ',' ',' ',' '],
                [' ',' ',' ','O',' ',' ',' '],
                [' ',' ',' ',' ','O',' ',' '],
                [' ',' ',' ',' ',' ',' ',' '],
                ['-',' ',' ',' ',' ',' ','-']], "X"]
k=5

# find all initial points that could lead to a k in a row horizontally for either side
#def findHoriz(intial):
#  #numrows=len(initial)
#  #numcolumns=len(intial[0])
#  goodSquares=[]
#  if numcolumns >=k:
#    for row in range(numrows):
#      for column in range(numcolumns):
#        colFlag=True
#        endCol = column+ k-1
#        if (initial[row][column]!='-') and endCol < numcolumns: # column can be used as starting column
#          for adjcol in range (column,endCol):
#            if initial[row][adjcol] == '-':
#              colflag = False
#          if colFlag== True:
#            goodSquares.append((row,column))
#  return goodSquares
#
#def findVert(intial):
#  #numrows=len(initial)
#  #numcolumns=len(intial[0])
#  goodSquares=[]
#  if numrows >=k:
#    for col in range(numcolumns):
#      for row in range(numrows):
#        rowFlag=True
#        endRow = row+ k-1
#        if (initial[row][col]!='-') and endRow < numrows: # column can be used as starting column
#          for adjrow in range (row+1,endRow+1):
#            if initial[adjrow][col] == '-':
#              rowFlag = False
#          if rowFlag == True:
#            goodSquares.append((row,col))
#  return goodSquares
#
#def findDiagonal(initial):
#  numrows=len(initial)
#  numcolumns=len(intial[0])
#  goodSquares=[]
#  for row in range(numrows):
#    for col in range(numcols):
#      current_square = initial[row][col]
#      if (current_square != 0):
#          pass
         
def prepare(initial_state, k, what_side_I_play, opponent_nickname):
  global initial
  global ktowin
  global side
  global opponent_nick
  global forbidden
  global numrows
  global numcolumns

  forbidden=[]
  initial=initial_state
  ktowin=k
  side =  what_side_I_play
  opponent_nick = opponent_nickname
  print('I am side ' + side)

  # get size of board
  numrows=len(initial)
  numcolumns=len(initial[0])
  print(numrows)
  print(numcolumns)

    # get location of forbidden squares
  #for row in range(numrows-1):
  #  for column in range(numcolumns-1):
  #    if initial_state[row][column] == '-':
  #      forbidden.append ([[row][column]])

    # do I need to know where handicaps are..? maybe not..

    # find all k that could win
    # scan board horizontally and find ones that win
    # scan vertically
    # scan diagonally
    #goodSquares = findHoriz(intial)
    #goodSquares.append (findVert(initial))
    #goodSquares.append (findDiag1(initial))
    #goodSquares.append (findDiag2(initial))

def introduce():
    return ("Hello, I am Ava, the super genious killing k-in-a-row machine /"
            "and I will show you how stupid you are in this game! My creator is /"
            "Stella Stylianidou (stellast@uw.edu) and Phil Synder(phil0@uw.edu)")

def nickname():
    return "Ava"

def generate_possible_moves(state):
    possible_moves = []
    for row in range(numcolumns):
        for col in range(numrows):
            if state[row][col] == ' ':
                possible_moves.append((row, col))
    return possible_moves


# need to do timeLimit
# maybe chose randomly if a lot have the same score? maybe dont calculate anything at the beginning?
def makeMove(currentState,currentRemark,timeLimit=10000):
    # caclulate move

    #start = time.time()
    #elapsed = 0
    #while elapsed < timeLimit:
    #    elapsed = time.time() - start

    currentState=currentState[0]
    best_move = minimax(currentState, 3, side)
    print(best_move)

    # calculate newState
    newState = deepcopy(currentState)
    newState[best_move[0][0]][best_move[0][1]] = side


    # remarks for a good static eval
    if stateval_for_side (newState) > 1000:
      newRemark = choice (["Haha! I bet you didn't see that coming.",
                                "Oh you poor human you are going to lose so badly.",
                                "Such a bad choice human",
                                "I am so looking forward to your end",
                                side + " for the win!",
                                "Such an awesome move on my behalf",
                                "I may be rocking this game.",
                                "You have no idea what's coming human"
                                ])
    elif stateval_for_side (newState) < 0: # remarks for bad static eval
      newRemark = choice (["Let me think about this.",
                                "Hmm.. I am smarter than you.. I don't understand.",
                                "Okay, I guess that's a valid move.",
                                "I can still kill you. I am smart.",
                                "I can't believe you just did that.",
                                "This doesn't look great."
                                "I will get back to you with a manuever you won't see."
                                ])
    else: # remarks for other states
      newRemark = choice (["So what are you doing next?",
                                "Wasn't my move the best move ever?",
                                "I am so good at this game.",
                                "Such an awesome move on my behalf",
                                "Your turn silly human.",
                                "This is so easy.",
                                "Oh how cute. Aren't you bad at this game?"
                                ])

    #print ('I am in side ' + side)

    return([[best_move[0], [newState,side]], newRemark])



def minimax(current_state, depth_level, what_side):
    if depth_level == 0:
        return [None, staticEval(current_state)]
    else:
        possible_moves = generate_possible_moves(current_state)
        if what_side == 'X':
            best_move_so_far = [possible_moves[0], float('-inf')]
        else:
            best_move_so_far = [possible_moves[0], float('inf')]
        for move in possible_moves:
            new_state = deepcopy(current_state)
            new_state[move[0]][move[1]] = what_side
            score = minimax(new_state, depth_level - 1, sub(what_side, '', 'XO'))
            if what_side == 'X':
                if score[1] > best_move_so_far[1]:
                    best_move_so_far = [move, score[1]]
            else:
                if score[1] < best_move_so_far[1]:
                    best_move_so_far = [move, score[1]]
        return best_move_so_far

def stateval_for_side (state):
    if side == 'X':
        return staticEval(state)
    else:
        return -staticEval(state)


def staticEval(state):
  # calculate how good this state is
  # high value is good for X, low value is good for O
  result = 0
  for num in range(2,k+1):
    xinarow = find_num_side(state,'X',num)
    oinarow = find_num_side(state,'O',num)

    #print('X ' + str(num) + ' in a row: ' +str(xinarow))
    #print('O '  + str(num) + ' in a row: ' +str(oinarow))
    if num == k and xinarow > 0:
        return float('inf')
    elif num == k and oinarow > 0:
        return float('-inf')
    else:
        result += pow(2, num) * xinarow - pow(2, num) * oinarow
        #result += pow(2.71,num * xinarow) - pow(2.71,num*oinarow)

  # calculate
  return result

# finds how many X's or O's
def find_num_side (state,side, num):
  counter=0
  numrows=len(state)
  numcolumns=len(state)

  # Horizontal
  for row in range(numrows):
    for col in range(numcolumns-num+1):
      if state[row][col]== side:
        flag = True
        for adjcol in range(col+1,col+num):
          if state[row][adjcol] !=side :
            flag=False
        if flag and (col+num+1 > numcolumns or state[row][col+num]!=side) and (col-1<0 or state[row][col-1]!=side):
          # print ('passed row ' + str(row) +  ' and col ' + str(col) + ' at end ' + str(col+num))
          counter = counter + 1

  # Vertical
  for col in range(numcolumns):
    for row in range(numrows-num+1):
      if state[row][col] == side:
        flag = True
        #print (str(flag)+' trying col ' + str(col) +  ' and row ' + str(row) + ' at end ' + str(row+num))
        for adjrow in range(row+1,row+num):
          #print(str(col) + ' ' +str(adjrow) + ' ' + str(state[adjrow][col]))
          if state[adjrow][col] != side :
            flag=False
        if flag and (row+num+1 > numrows or state[row+num][col]!=side) and (row-1<0 or state[row-1][col]!=side):
          #print ('passed row ' + str(row) +  ' and col ' + str(col) + ' at end ' + str(col+num))
          counter = counter + 1

  # Diagonal
  for row in range(numrows):
    for col in range(numcolumns):
      backslash = [(row+increment, col+increment) for increment in range(num)]
      forwardslash = [(row+increment, col-increment) for increment in range(num)]
      k_in_a_row_backslash_is_here = True
      try:
        for coord in backslash:
          if state[coord[0]][coord[1]] != side:
            k_in_a_row_backslash_is_here = False
        try:
          if state[coord[0] + 1][coord[1] + 1] == side or state[row-1][col-1] == side:
            k_in_a_row_backslash_is_here = False
        except IndexError:
          pass
      except IndexError:
        k_in_a_row_backslash_is_here = False
      if k_in_a_row_backslash_is_here:
        counter += 1
      k_in_a_row_forwardslash_is_here = True
      try:
        for coord in forwardslash:
          if state[coord[0]][coord[1]] != side:
            k_in_a_row_forwardslash_is_here = False
        try:
          if state[coord[0] + 1][coord[1] - 1] == side or state[row-1][col+1] == side:
            k_in_a_row_forwardslash_is_here = False
        except IndexError:
          pass
      except IndexError:
        k_in_a_row_forwardslash_is_here = False
      if k_in_a_row_forwardslash_is_here:
        counter += 1
  return counter

#prepare(test[0], 3, 'X', 'Jacob')
#makeMove(test[0], 'hi')
