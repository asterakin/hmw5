


initial =\
    [['-','X','X','X','X','O','-'],
    [' ','X',' ','O',' ',' ',' '],
    [' ','X',' ',' ',' ',' ',' '],
    [' ','X','X','X','X','X','O'],
    [' ','O',' ',' ',' ',' ',' '],
    [' ','O','O','O',' ',' ',' '],
    ['-',' ',' ',' ',' ',' ','-']]
k=5


# find all initial points that could lead to a k in a row horizontally for either side
def findHoriz(intial):
  #numrows=len(initial)
  #numcolumns=len(intial[0])
  goodSquares=[]
  if numcolumns >=k:
    for row in range(numrows):
      for column in range(numcolumns):
        colFlag=True
        endCol = column+ k-1
        if (initial[row][column]!='-') and endCol < numcolumns: # column can be used as starting column
          for adjcol in range (column,endCol):
            if initial[row][adjcol] == '-':
              colflag = False
          if colFlag== True:
            goodSquares.append((row,column))
  return goodSquares


def findVert(intial):
  #numrows=len(initial)
  #numcolumns=len(intial[0])
  goodSquares=[]
  if numrows >=k:
    for col in range(numcolumns):
      for row in range(numrows):
        rowFlag=True
        endRow = row+ k-1
        if (initial[row][col]!='-') and endRow < numrows: # column can be used as starting column
          for adjrow in range (row+1,endRow+1):
            if initial[adjrow][col] == '-':
              rowFlag = False
          if rowFlag == True:
            goodSquares.append((row,col))
  return goodSquares


def prepare(initial_state, k, what_side_I_play, opponent_nickname):
  global initial
  global ktowin
  global side
  global opponent_nick
  global forbidden
  global numrows
  global numcolumns

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
  result = 0
  for num in range(2,k+1):
    xinarow = find_num_side(state,'X',num)
    oinarow = find_num_side(state,'O',num)
    print('X ' + str(num) + ' in a row: ' +str(xinarow))
    print('O '  + str(num) + ' in a row: ' +str(oinarow))
    result += num * 10 * xinarow - num* 10 * oinarow

  # calculate
  return result


# finds how many X's or O's
def find_num_side (state,side, num):
  counter=0
  numrows=len(state)
  numcolumns=len(state[0])

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

  return counter


#print (initial[6][2])
#print(find_num_side(initial,'O',2))
#goodSqr = findHoriz(initial)
#goodSqr.append(findVert(initial))
print(staticEval(initial))
