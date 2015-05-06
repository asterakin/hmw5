__author__ = 'Stella'



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
