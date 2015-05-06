from copy import deepcopy 
from re import sub
from random import choice
import time

         
def prepare(initial_state, k, what_side_I_play, opponent_nickname):
  global initial
  global kToWin
  global side
  global opponent_nick
  global forbidden
  global numrows
  global numcolumns

  forbidden=[]
  initial=initial_state[0]
  kToWin=k
  side =  what_side_I_play
  opponent_nick = opponent_nickname


  numrows=len(initial)
  numcolumns=len(initial[0])

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

def makeMove(currentState,currentRemark,timetemp=10000):
    global start
    global elapsed
    start = time.time()
    elapsed = 0
    global timeLimit
    timeLimit=timetemp




    currentState=currentState[0]
    best_move = minimax(currentState, 2, side)

    newState = deepcopy(currentState)
    newState[best_move[0][0]][best_move[0][1]] = side


    # remarks for a good static eval
    if stateval_for_side (newState) > pow(2,kToWin-2):
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


    if side=='X':
        otherside='O'
    else:
        otherside='X'
        
    return([[best_move[0], [newState,otherside]], newRemark])

def minimax(current_state, depth_level, what_side):
    possible_moves = generate_possible_moves(current_state)
    elapsed = time.time() - start
    if find_num_side(current_state,'X',kToWin)>0:
        return [None, float('inf')]
    if find_num_side(current_state,'O',kToWin)>0:
        return [None, float('-inf')]
    if possible_moves == [] or depth_level == 0:
        return [None, staticEval(current_state)]
    else:
        if what_side == 'X':
            best_move_so_far = [possible_moves[0], float('-inf')]
        else:
            best_move_so_far = [possible_moves[0], float('inf')]
        for move in possible_moves:
            new_state = deepcopy(current_state)
            new_state[move[0]][move[1]] = what_side
            if  timeLimit - elapsed <= 0.15:
                return best_move_so_far
            else:
                score = minimax(new_state, depth_level - 1, sub(what_side, '', 'XO'))
                if what_side == 'X':
                    if score[1] >= best_move_so_far[1]:
                        best_move_so_far = [move, score[1]]
                else:
                    if score[1] <= best_move_so_far[1]:
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
  for num in range(2,kToWin+1):
    xinarow = find_num_side(state,'X',num)
    oinarow = find_num_side(state,'O',num)

    if num == kToWin and xinarow > 0:
        return float('inf')
    elif num == kToWin and oinarow > 0:
        return float('-inf')
    else:
        result += pow(2, num) * xinarow - pow(2, num) * oinarow

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
        if flag and (num==kToWin or ((col+num+1 > numcolumns or state[row][col+num]!=side) and (col-1<0 or state[row][col-1]!=side))):
          counter = counter + 1

  # Vertical
  for col in range(numcolumns):
    for row in range(numrows-num+1):
      if state[row][col] == side:
        flag = True
        for adjrow in range(row+1,row+num):
          if state[adjrow][col] != side :
            flag=False
        if flag and (num==kToWin or (((row+num+1 > numrows or state[row+num][col]!=side) and (row-1<0 or state[row-1][col]!=side)))):
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
