
initial =[['-',' ',' ',' ',' ',' ','-'],
                [' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' '],
                ['-',' ',' ',' ',' ',' ','-']]
k=5


# find all initial points that could lead to a k in a row horizontally for either side
def findHoriz(intial):
  numrows=len(initial)
  numcolumns=len(intial[0])
  goodSquares=[]
  if numcolumns >=k:
    for row in range(numrows):
      for column in range(numcolumns):
        colFlag=True
        endCol = column+ k-1
        if (initial[row][column]!='-') and endCol < numcolumns: # column can be used as starting column
          for adjcol in range (column,endCol):
            if initial[row][adjcol] != '-':
              colflag = False
          if colFlag== True:
            goodSquares.append((row,column))
  return goodSquares


def findVert(intial):
  numrows=len(initial)
  numcolumns=len(intial[0])
  goodSquares=[]
  if numrows >=k:
    for col in range(numcolumns):
      for row in range(numrows):
        rowFlag=True
        endRow = row+ k-1
        if (initial[row][col]!='-') and endRow < numrows: # column can be used as starting column
          for adjrow in range (row,endRow):
            if initial[adjrow][col] != '-':
              rowFlag = False
          if rowFlag== True:
            goodSquares.append((row,col))
  return goodSquares


def prepare(initial_state, k, what_side_I_play, opponent_nickname):
  global initial
  global ktowin
  global side
  global opponent_nick
  global forbidden

  forbidden=[]
  initial=initial_state[0]
  ktowin=k
  side =  what_side_I_play
  opponent_nick = opponent_nickname

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
    goodSquares = findHoriz(intial)
    goodSquares.append (findVert(initial))
    goodSquares.append (findDiag1(initial))
    goodSquares.append (findDiag2(initial))



def introduce():
    return ("Hello, I am the Eva, the super genious killing k-in-a-row machine /"
            "and I will show you how stupid you are in this game! My creator is /"
            "Stella Stylianidou (stellast@uw.edu) and Phil Synder(phil0@uw.edu)")

def nickname():
    return "Eva"

def makeMove(currentState,currentRemark,timeLimit=10000):

    # caclulate move


    # calculate newState

    # returnsomeRemark
    return()

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


print(findVert(initial))