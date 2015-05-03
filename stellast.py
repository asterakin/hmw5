__author__ = 'Stella'


def findHor(intial):
  side='X'
  numrows=len(initial)
  numcolumns=len(intial[0])
  goodSquares=[]
  if numcolumns >=k:
    for row in range(numrows-1):
      for column in range(numcolumns-1):
        colFlag=True
        endCol = initial_state[row][column]+ k
        if (initial_state[row][column] =side or initial_state[row][column] =' ') and endCol < numcolumns-1: # column can be used as starting column
          for adjcol in range (column,numcolumns-1):
            if initial_state[row][adjcol] != ' ' or initial_state[row][adjcol] != side:
              colflag = False
          if colFlag=True:
            for x in range(column,endCol):
              goodSquares.append ([row][x])
  return goodSquares


def prepare(initial_state, k, what_side_I_play, opponent_nickname):
  global initial
  global k
  global side
  global opponent_nickname
  global forbidden

  forbidden=[]
  initial=initial_state[0]
  k=k
  side =  what_side_I_play
  opponent_nickname = opponent_nickname

  # get size of board
  numrows=len(initial)
  numcolumns=len(intial[0])

    # get location of forbidden squares
  for row in range(numrows-1):
    for column in range(numcolumns-1):
      if initial_state[row][column] == '-':
        forbidden.append ([[row][column]])

    # do I need to know where handicaps are..? maybe not..


    # find all k that could win
    # scan board horizontally and find ones that win
    # scan vertically
    # scan diagonally
    goodSquares = findHor(intial)
    goodSquares.append (findVert(initial))
    goodSquares.append (findDiag1(initial))
    goodSquares.append (findDiag2(initial))



def introduce():
    return ("Hello, I am the Eva, the super genious killing k-in-a-row machine /"
            "and I will show you how stupid you are in this game! My creator is /"
            "Stella Stylianidou (stellast@uw.edu) and Phil Synder(phil0@uw.edu)")

def nickname():
    return "Eva"

def makeMove(currentState,currentRemark,timeLimit=10000)

    # caclulate move


    # calculate newState

    # returnsomeRemark

def staticEval(state):
    # calculate how good this state is

    # find how many 5'X's in a row and O's
    fiveX =0
    fiveO =0

    # find how many 4'X's in a row
    fourX =0
    fourO =0
    # 3
    threeX=0
    threeO=0
    # 2
    twoX =0
    twoO=0
    # 1
    oneX =0
    oneO=0

    # calculate
    return 100*fiveX + 80*fourX+60*threeX+30*twoX+10*oneX-100*fiveO-80*fourO-60*threeO-30*twoO-10*oneO


