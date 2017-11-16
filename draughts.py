import random
def instruction(): #Explains how to use the game
    print("Welcome to a game of draughts. Player 1. Select your Opponent. You have a choice of two. Agaisnt your frind or Play agasint the computer")
    print("Rules:")
    print("     1. The format of the cordinates is 0.0")
    print("     2. Each will take turn to move")
    print("     3. The game will end when someone has no pieces left")
    print("     4. Double jumping is NOT allowed")
    print("     5. Pieces are only allowed to move 1 spot at a time only if they are stealing an opponents piece")
    print("     6. To undo a move, write 'undo' on your opponents")
    print("     7. Player 1 = 'B' & Player 2 = 'W' ")
    print("     8. Kings will be changed to 'b' & 'w'\n") #\n is a new line



def init_board(): #Intializes the board :
    grid = [[0 for x in range(width)] for y in range(height)] # creates the list 

    for x in range(width):
        print("")
        for y in range(height):
            if(x <3 and (y%2)!=0): #Sets Players 1 pieces
                if((x%2)== 0): # if x is divisable by 2 is 0 then sets sqaure to B
                    grid[x][y] = "B "
                else:
                    grid[x][y] = "| " # if x is divisable by 2 is 0 then sets sqaure |
            elif (x <3 and (y%2)==0):
                if((x%2)!= 0):
                    grid[x][y] = "B "
                else:
                    grid[x][y] = "| "

            if((x >2 and x <5) and ((y%2)!=0)): #sets the middle sqaures
                if((x%2)== 0):
                    grid[x][y] = "_ "
                else:
                    grid[x][y] = "| "
            elif ((x >2 and x <5) and (y%2)==0):
                if((x%2)!= 0):
                    grid[x][y] = "_ "
                else:
                    grid[x][y] = "| "
                
            
            
            if(x >4 and (y%2)!=0): #Sets players 2 pieces
                if((x%2)== 0):
                    grid[x][y] = "W "
                else:
                    grid[x][y] = "| "
            elif (x >4 and (y%2)==0):
                if((x%2)!= 0):
                    grid[x][y] = "W "
                else:
                    grid[x][y] = "| "

        

    draw_grid(grid) #Function to draw the grid
    return grid

def stilPieces(): #checks and counts the pieces on the board
    countB = 12
    countW = 12
    checkB = 0
    checkW = 0
    
    for i in range(8):
        for j in range(8):
            if(grid[i][j] == "B " or grid[i][j] =="b "):
                checkB = checkB +1 #checks how many places on the board
            elif(grid[i][j] == "W " or grid[i][j] == "w "):
                checkW = checkW +1
                
    defB = countB - checkB # defB checks the difference between 12 and the remaining spots
    countB = countB - defB # updates the countB
    print("Count B",countB)
  
    defW = countW -checkW
    countW = countW - defW
    print("Count W",countW)

    if(countB > 0 or countW > 0): #Continues the game
        return False
    elif(countB == 0 or countW == 0 ): #ends the game
        return True
   
def draw_grid(grid):
    print("   0 1 2 3 4 5 6 7") #prints y's coordinates
    for x in range(width):
        print("")
        print(x," ",end="") #helps with x's coordinates
        for y in range(height):
            print(grid[x][y], end="")
    return grid
        
def firstMove(i):
    print("Player 1's Turn")
    draw_grid(grid)
    response = False

    currentMove1.append(input("Select piece to move"))
    while(currentMove1[i] == "" and response == False):

            
        if(currentMove1[i]== ""): #checks if the sqaure is empty then tries again
            currentMove1.pop()
            currentMove1.append(input("Select piece to move"))
    else:
        response = True
        print(currentMove1)
        
    if(currentMove1[i] == "redo"): #checks if the item is redo
        currentMove1.pop() #removes redo from the stack
        redoFeature(i, pastMove1, currentMove1)
            
    if(currentMove1[i] == "undo"):
         currentMove1.pop()
         undo_feature_2(j,pastMove2,currentMove2,redoFeature2POS1,redoFeature2POS2)
    else:
        validPOS1(currentMove1, pastMove1,i) #Another Function
        stilPieces()
    return grid

def validPOS1(currentMove1,pastMove1,i): #checks if the postion is correct
    toRows  = int (currentMove1[i][0:1]) #Converts the sliced string to an int
    toCols  = int (currentMove1[i][2:3])

    avaPOSX = toRows + 1 #chnages the coordinates to llok for the avaliable spaces near by
    avaPOSL = toCols - 1
    avaPOSR = toCols + 1

    POSX = toRows + 2
    POSL = toCols - 2
    POSR = toCols + 2


    if(grid[toRows][toCols] == "b "): #checks for a king piece
    
        kingMoves(toRows, toCols,i, pastMove1,currentMove1)
    else:
        
        response = False
        
        if((toRows < 0 or toRows >7) or (toCols < 0 or toCols > 7)): #checks if the input is in range
            if((avaPOSX <0 or avaPOSX > 7) or (avaPOSL <0 or avaPOSL >7) or (avaPOSR <0 and avaPOSR >7)):#checka whether the avalaible pos are in range
                print("Out of Range")
                currentMove1.append(input("Select piece to move"))
                toRows  = int (currentMove1[i][0:1]) #Converts the sliced string to an int
                toCols  = int (currentMove1[i][2:3])

                avaPOSX = toRows + 1 # the postion diagonal from the one given
                avaPOSL = toCols - 1 
                avaPOSR = toCols + 1
          
            while(((grid[toRows][toCols]!= "B ")or(grid[avaPOSX][avaPOSL] != "_ ") or (grid[avaPOSX][avaPOSR] != "_ ") or (grid[POSX][POSR] != "_ ")
                   or( grid[POSX][POSL] != "_ "))  and response == False):
                
                if(grid[toRows][toCols]== "B "):
                    response = True
                    
                if (grid[avaPOSX][avaPOSL] == "_ " ): #if the ava POS has a space
                    response = True

                if (grid[POSX][POSL] == "_ " ): # check if there was a free spot 2 spaces away and then checks if pplayer 2 is a spot away. 
                    if(grid[avaPOSX][avaPOSL] == "W " or grid[avaPOSX][avaPOSL] == "w "): 
                        response = True
            
                elif (grid[avaPOSX][avaPOSR] == "_ "): 
                    response = True
           
            
                elif(grid[POSX][POSR] == "_ "):
                    if(grid[avaPOSX][avaPOSR] == "W " or grid[avaPOSX][avaPOSR] == "w " ):
                        response = True
                    
                
                if((grid[toRows][toCols] != "B ")or(grid[avaPOSX][avaPOSL] != "_ ") and (grid[avaPOSX][avaPOSR] != "_ ") and (grid[POSX][POSR] != "_ ") and (grid[POSX][POSL] != "_ ")):

                        currentMove1.pop()
                        currentMove1.append(input("Selcet A Moveable Piece"))
                        toRows  = int (currentMove1[i][0:1]) 
                        toCols  = int (currentMove1[i][2:3])

                        avaPOSX = toRows + 1 #changes the coordinates to look for the avaliable spaces near by
                        avaPOSL = toCols - 1
                        avaPOSR = toCols + 1   
           
                            
    pastMove1.append(input("Select New Postion")) #asks the user for the new position 
    print(pastMove1)

    newPOSX  = int(pastMove1[i][0:1]) #temp coordinates
    newPOSY  =  int(pastMove1[i][2:3])
    re = False

    while(grid[newPOSX][newPOSY] != "_ " and re ==False): #loops while the new position is not avaliable
                
        if (grid[newPOSX][newPOSY] != "_ "):
             pastMove1.pop(i)
             pastMove1.append(input("Unvalid Move! Select A New Postion"))
             newPOSX  = int (pastMove1[i][0:1]) #temp coordinates
             newPOSY  = int (pastMove1[i][2:3])
             
    else:
        re = True
        grid[newPOSX][newPOSY] = "B "  #changes the avilabe space to B and the last space to _
        grid[toRows][toCols] = "_ "
        checkForOpponents(newPOSX, newPOSY, toRows ,toCols)
        checkStatus(newPOSX, newPOSY)

        return pastMove1, grid, toRows,toCols, i 


def checkForOpponents(newPOSX, newPOSY, toRows ,toCols): #Steals opponents piece if possible

    if ((newPOSY-toCols) == 2): #this will deterine in which direction it goes
        #Sqaure moves right 
        a = newPOSX - 1 #a and b coorindinates for opponent
        b = newPOSY - 1 
        if(grid[a][b] == "W " or (grid[a][b] == "w ")):
            grid[a][b] = "_ " #overwrites opponents piece.     
            replayFeature(i,pastMove1,currentMove1,a,b)
            
            
    if (newPOSY-toCols == -2): #sqaure moved left
      
        a = newPOSX -1
        b = newPOSY + 1
        
        if(grid[a][b] == "W " or (grid[a][b] == "w ")):
            grid[a][b] = "_ "
            replayFeature(i,pastMove1,currentMove1,a,b)

    return

def checkStatus(newPOSX, newPOSY): # checks if king

    if(newPOSX == 7):
        grid[newPOSX][newPOSY] = "b "
    else:
        return False
    

def kingMoves(toRows, toCols,i, pastMove1,curentMove1): #simialr to valid move but for the king pieces
    avaPOSX = toRows + 1
    avaPOSY = toRows - 1
    avaPOSL = toCols - 1
    avaPOSR = toCols + 1

    
    #Valid pos
    POSX = toRows + 2 # Spaces free. Part of stealing an oppoents piece
    POSY = toRows - 2
    POSL = toCols - 2
    POSR = toCols + 2

    response = False
    
    if((toRows < 0 or toRows >7) or (toCols < 0 or toCols > 7)):
        if((avaPOSX <0 or avaPOSX > 7) or (avaPOSY <0 or avaPOSY > 7) or
           (avaPOSL <0 or avaPOSL >7) or(avaPOSR <0 and avaPOSR >7)):   
            print("Out of Range")
            currentMove1.append(input("Select piece to move"))
            toRows  = int (currentMove1[i][0:1]) #Converts the sliced string to an int
            toCols  = int (currentMove1[i][2:3])

            avaPOSX = toRows + 1
            avaPOSY = toRows - 1
            avaPOSL = toCols - 1
            avaPOSR = toCols + 1
            
            
        else:
            while(((grid[avaPOSX][avaPOSL] != "_ ") or (grid[avaPOSX][avaPOSR] != "_ ") or(grid[avaPOSY][avaPOSL] != "_ ") or(grid[avaPOSY][avaPOSR] != "_ ")
                   or (grid[POSX][POSR] != "_ ") or(grid[POSX][POSL] != "_ ") or (grid[POSY][avaPOSL] != "_ ") or (grid[POSY][avaPOSR] != "_ "))  and response == False):

                if (grid[avaPOSX][avaPOSL] == "_ " ):
                    response = True
                    
                if(grid[avaPOSY][avaPOSL] == "_ "):
                    response = True

                if (grid[POSX][POSL] == "_ " ):
                    if(grid[avaPOSX][avaPOSL] == "W " or grid[avaPOSX][avaPOSL] == "w "):
                        response = True
                        
                if(grid[POSY][POSL] == "_ "):
                    if(grid[avaPOSY][avaPOSL] == "W " or grid[avaPOSY][avaPOSL] == "w "):
                        response = True
            
                elif (grid[avaPOSX][avaPOSR] == "_ "):
                    response = True
                    
                elif(grid[avaPOSY][avaPOSR] == "_ "):
                     response = True
            
                elif(grid[POSX][POSR] == "_ "):
                    if(grid[avaPOSX][avaPOSR] == "W " or grid[avaPOSX][avaPOSR] == "w "):
                        response = True
                    
                elif(grid[POSY][POSR] == "_ "):
                    if(grid[avaPOSY][avaPOSR] == "W " or grid[avaPOSY][avaPOSR] == "w "):
                        response = True
                        
                if((grid[avaPOSX][avaPOSL] != "_ ") and (grid[avaPOSX][avaPOSR] != "_ ") and (grid[POSX][POSR] != "_ ") and (grid[POSX][POSL] != "_ ")
                   and (grid[avaPOSY][avaPOSL] != "_ ") and (grid[avaPOSY][avaPOSR] != "_ ") and (grid[POSY][POSR] != "_ ") and (grid[POSY][POSL] != "_ ")):
                        currentMove = input("Selcet A Moveable Piece")
                        toRows  = int (currentMove[0:1]) #Converts the sliced string to an int
                        toCols  = int (currentMove[2:3])

                        avaPOSX = toRows + 1
                        avaPOSY = toRows - 1 #chnages the coordinates to llok for the avaliable spaces near by
                        avaPOSL = toCols - 1
                        avaPOSR = toCols + 1
       
                        
        pastMove1.append(input("Select New Postion"))
        print(pastMove1)

        newPOSX  = int(pastMove1[i][0:1]) #temp coordinates
        newPOSY  =  int(pastMove1[i][2:3])
        re = False

        while(grid[newPOSX][newPOSY] != "_ " and re ==False):
                    
            if (grid[newPOSX][newPOSY] != "_ "):
                 pastMove1.pop()
                 pastMove1.append(input("Unvalid Move! Select A New Postion"))
                 newPOSX  = int (pastMove1[i][0:1]) #temp coordinates
                 newPOSY  = int (pastMove1[i][2:3])
                 
        else:
            re = True
            grid[newPOSX][newPOSY] = "B "  #changes the avilabe space to B and the last space to _
            grid[toRows][toCols] = "_ "
            checkForOpponents(newPOSX, newPOSY, toRows ,toCols)
            king1 = checkStatus(newPOSX, newPOSY)
            
        
    
    return grid

def kingOpponents(newPOSX, newPOSY, toRows ,toCols): #simialr to opponents but for kings only
    if ((newPOSY - toCols) == 2):  #Sqaure moves right 
        if((newPOSX - toRows) == 2): #sqaure moved down
           
            a = newPOSX - 1 #a and b coorindinates for opponent
            b = newPOSY - 1 
            if(grid[a][b] == "W " or grid[a][b] == "w "):
                grid[a][b] = "_ "
                
        elif((newPOSX-toRows)== -2): #sqaure moved up
            a = newPOSX + 1 #a and b coorindinates for opponent
            b = newPOSY - 1
            print() 
            if(grid[a][b] == "W " or grid[a][b] == "w "):
                grid[a][b] = "_ "
        
        
            
    if (newPOSY-toCols == -2): #sqaure moved left
         if((newPOSX - toRows) == 2): #sqaure moved down
           
            a = newPOSX - 1 #a and b coorindinates for opponent
            b = newPOSY + 1
            if(grid[a][b] == "W " or grid[a][b] == "w "):
                grid[a][b] = "_ "
                
         elif((newPOSX-toRows)== -2): #sqaure moved up
            a = newPOSX + 1 #a and b coorindinates for opponent
            b = newPOSY + 1
            
            if(grid[a][b] == "W " or grid[a][b] == "w "):
                grid[a][b] = "_ "

    return newPOSX, newPOSY, toRows ,toCols

def secondMoves(j): #second players turn
    print("Player 2's Turn")
    draw_grid(grid)
    response = False
    
    currentMove2.append(input("Select piece to move"))
    while(currentMove2[j] == "" and response == False):
        if(currentMove2[j]== ""):
            currentMove2.pop()
            currentMove2.append(input("Select piece to move"))
    else:
        response = True
        print(currentMove2)
        
    if(currentMove2[j] == "redo"):
        currentMove2.pop()
        redo_feature2(j, pastMove2, currentMove2)
            
    if(currentMove2[j] == "undo"):
        currentMove2.pop()
        undo_feature(i,pastMove1,currentMove1,redoFeaturePOS1,redoFeaturePOS2)
    else:
        validPOS2(currentMove2, pastMove2,j) #Another Function
    return grid


def validPOS2(currentMove2, pastMove2,j):
    toRows  = int (currentMove2[j][0:1]) #Converts the sliced string to an int
    toCols  = int (currentMove2[j][2:3])

    avaPOSX = toRows + 1 #chnages the coordinates to llok for the avaliable spaces near by
    avaPOSL = toCols - 1
    avaPOSR = toCols + 1

    POSX = toRows + 2
    POSL = toCols - 2
    POSR = toCols + 2


    if(grid[toRows][toCols] == "w "):
    
        kingMoves(toRows, toCols,j, pastMove2,currentMove2)
    else:
        
        response = False
        
        if((toRows < 0 or toRows >7) or (toCols < 0 or toCols > 7)): #checks if the input is in range
            if((avaPOSX <0 or avaPOSX > 7) or (avaPOSL <0 or avaPOSL >7) or (avaPOSR <0 and avaPOSR >7)):#checka whether the avalaible pos are in range
                print("Out of Range")
                currentMove1.append(input("Select piece to move"))
                toRows  = int (currentMove2[j][0:1]) #Converts the sliced string to an int
                toCols  = int (currentMove2[j][2:3])

                avaPOSX = toRows + 1
                avaPOSL = toCols - 1
                avaPOSR = toCols + 1
          
            while(((grid[toRows][toCols]!= "W ")or(grid[avaPOSX][avaPOSL] != "_ ") or (grid[avaPOSX][avaPOSR] != "_ ") or (grid[POSX][POSR] != "_ ")
                   or( grid[POSX][POSL] != "_ "))  and response == False):
                
                if(grid[toRows][toCols]== "W "):
                    response = True
                    
                if (grid[avaPOSX][avaPOSL] == "_ " ): #if the ava POS has a space
                    response = True

                if (grid[POSX][POSL] == "_ " ): # check if there was a free spot 2 spaces away and then checks if pplayer 2 is a spot away. 
                    if(grid[avaPOSX][avaPOSL] == "B " or grid[avaPOSX][avaPOSL] == "b "): 
                        response = True
            
                elif (grid[avaPOSX][avaPOSR] == "_ "): 
                    response = True
           
            
                elif(grid[POSX][POSR] == "_ "):
                    if(grid[avaPOSX][avaPOSR] == "B " or grid[avaPOSX][avaPOSR] == "b " ):
                        response = True
                    
                
                if((grid[toRows][toCols] != "W ")or(grid[avaPOSX][avaPOSL] != "_ ") and (grid[avaPOSX][avaPOSR] != "_ ") and (grid[POSX][POSR] != "_ ") and (grid[POSX][POSL] != "_ ")):

                        currentMove2.pop()
                        currentMove2.append(input("Selcet A Moveable Piece"))
                        toRows  = int (currentMove2[j][0:1]) #Converts the sliced string to an int
                        toCols  = int (currentMove2[j][2:3])

                        avaPOSX = toRows + 1 #chnages the coordinates to llok for the avaliable spaces near by
                        avaPOSL = toCols - 1
                        avaPOSR = toCols + 1   
               
                            
    pastMove2.append(input("Select New Postion"))
    print(pastMove2)

    newPOSX  = int(pastMove2[j][0:1]) #temp coordinates
    newPOSY  =  int(pastMove2[j][2:3])
    re = False

    while(grid[newPOSX][newPOSY] != "_ " and re ==False):
                
        if (grid[newPOSX][newPOSY] != "_ "):
             pastMove2.pop(j)
             pastMove2.append(input("Unvalid Move! Select A New Postion"))
             newPOSX  = int (pastMove2[j][0:1]) #temp coordinates
             newPOSY  = int (pastMove2[j][2:3])
             
    else:
        re = True
        grid[newPOSX][newPOSY] = "W "  #changes the avilabe space to B and the last space to _
        grid[toRows][toCols] = "_ "
        checkForOppo(newPOSX, newPOSY, toRows ,toCols)
        check2Status(newPOSX, newPOSY)

        return pastMove2, grid, toRows,toCols

def checkForOppo(newPOSX, newPOSY, toRows ,toCols): # only works when postions are valid.
    if ((newPOSY-toCols) == 2):
        #Sqaure moved right 
        a = newPOSX + 1 #a and b coorindinates for opponent
        b = newPOSY - 1
        
        if(grid[a][b] == "B " or grid[a][b] == "b "):
            grid[a][b] = "_ "
            replayFeature2(j,currentMove2,pastMove2,a,b)
        
            
    if (newPOSY-toCols == -2): #sqaure moved left
        a = newPOSX + 1
        b = newPOSY + 1
        if(grid[a][b] == "B " or grid[a][b] == "b "):
            grid[a][b] = "_ "
            replayFeature2(j,currentMove2,pastMove2,a,b)

    return 

def check2Status(newPOSX, newPOSY):

    if(newPOSX == 0):
        grid[newPOSX][newPOSY] = "w "
    else:
        return False

def king2Moves(toRows, toCols, j, pastMove2):
    avaPOSX = toRows - 1
    avaPOSY = toRows + 1
    avaPOSL = toCols - 1
    avaPOSR = toCols + 1
    
    
    #Valid pos
    POSX = toRows + 2
    POSY = toRows - 2
    POSL = toCols - 2
    POSR = toCols + 2

    response = False
    
    if((toRows < 0 or toRows >7) or (toCols < 0 or toCols > 7)):
        if((avaPOSX <0 or avaPOSX > 7) or (avaPOSL <0 or avaPOSL >7) or (avaPOSR <0 and avaPOSR >7)):   
            print("Out of Range")
            currentMove2.append(input("Select piece to move"))
            toRows  = int (currentMove2[j][0:1]) #Converts the sliced string to an int
            toCols  = int (currentMove2[j][2:3])

            avaPOSX = toRows + 1
            avaPOSY = toRows -1
            avaPOSL = toCols - 1
            avaPOSR = toCols + 1
            
            
        else:
            while(((grid[avaPOSX][avaPOSL] != "_ ") or (grid[avaPOSX][avaPOSR] != "_ ") or(grid[avaPOSY][avaPOSL] != "_ ") or(grid[avaPOSY][avaPOSR] != "_ ")
                   or (grid[POSX][POSR] != "_ ") or(grid[POSX][POSL] != "_ ") or (grid[POSY][avaPOSL] != "_ ") or (grid[POSY][avaPOSR] != "_ "))  and response == False):

                if (grid[avaPOSX][avaPOSL] == "_ " ):
                    response = True
                    
                if(grid[avaPOSY][avaPOSL] == "_ "):
                    response = True

                if (grid[POSX][POSL] == "_ " ):
                    if(grid[avaPOSX][avaPOSL] == "B " or grid[avaPOSX][avaPOSL] == "b "):
                        response = True
                        
                if(grid[POSY][POSL] == "_ "):
                    if(grid[avaPOSY][avaPOSL] == "B " or grid[avaPOSY][avaPOSL] == "b "):
                        response = True
            
                elif (grid[avaPOSX][avaPOSR] == "_ "):
                    response = True
                    
                elif(grid[avaPOSY][avaPOSR] == "_ "):
                     response = True
            
                elif(grid[POSX][POSR] == "_ "):
                    if(grid[avaPOSX][avaPOSR] == "B " or grid[avaPOSX][avaPOSR] == "b "):
                        response = True
                    
                elif(grid[POSY][POSR] == "_ "):
                    if(grid[avaPOSY][avaPOSR] == "B " or grid[avaPOSY][avaPOSR] == "b "):
                        response = True
                        
                if((grid[avaPOSX][avaPOSL] != "_ ") and (grid[avaPOSX][avaPOSR] != "_ ") and (grid[POSX][POSR] != "_ ") and (grid[POSX][POSL] != "_ ")
                   and (grid[avaPOSY][avaPOSL] != "_ ") and (grid[avaPOSY][avaPOSR] != "_ ") and (grid[POSY][POSR] != "_ ") and (grid[POSY][POSL] != "_ ")):
                        currentMove2.append(input("Select piece to move"))
                        toRows  = int (currentMove2[j][0:1]) #Converts the sliced string to an int
                        toCols  = int (currentMove2[j][2:3])

                        avaPOSX = toRows + 1
                        avaPOSY = toRows - 1 #chnages the coordinates to llok for the avaliable spaces near by
                        avaPOSL = toCols - 1
                        avaPOSR = toCols + 1
       
                        
            
    pastMove2.append(input("Select New Postion"))
    print(pastMove2)

    newPOSX  = int (pastMove2[j][0:1]) #temp coordinates
    newPOSY  = int (pastMove2[j][2:3])
        
    if (grid[newPOSX][newPOSY] == "_ "):  
      
        grid[newPOSX][newPOSY] = "w "  #changes the avilabe space to B and the last space to _
        grid[toRows][toCols] = "_ "
        kingOppo(newPOSX, newPOSY, toRows  ,toCols)
                        
    
    elif (grid[newPOSX][newPOSY] != "_ "):
         pastMove1 = input("Unvalid Move! Select A New Postion")
         newPOSX  = int (pastMove1[0:1]) #temp coordinates
         newPOSY  = int (pastMove1[2:3])
    
        
    
    return grid

def kingOppo(newPOSX, newPOSY, toRows ,toCols):
    if ((newPOSY - toCols) == 2):  #Sqaure moves right 
        if((newPOSX - toRows) == 2): #sqaure moved down
           
            a = newPOSX - 1 #a and b coorindinates for opponent
            b = newPOSY - 1 
            if(grid[a][b] == "B " or grid[a][b] == "b "):
                grid[a][b] = "_ "
        
        elif((newPOSX-toRows)== -2): #sqaure moved up
            a = newPOSX + 1 #a and b coorindinates for opponent
            b = newPOSY - 1
           
            if(grid[a][b] == "B " or grid[a][b] == "b "):
                grid[a][b] = "_ "
        
            
    if (newPOSY-toCols == -2): #sqaure moved left
         if((newPOSX - toRows) == 2): #sqaure moved down
           
            a = newPOSX - 1 #a and b coorindinates for opponent
            b = newPOSY + 1
            if(grid[a][b] == "B " or grid[a][b] == "b "):
                grid[a][b] = "_ "

         elif((newPOSX-toRows)== -2): #sqaure moved up
            a = newPOSX + 1 #a and b coorindinates for opponent
            b = newPOSY + 1
            
            if(grid[a][b] == "B " or grid[a][b] == "b "):
                grid[a][b] = "_ "                

def AI1Moves(i): #AI Player 1
    print("Player 1")
    draw_grid(grid)
    for r in range(height):
        for c in range(width):
            if(grid[r][c] == "B "): #Looks for its own pieces
                 checkIf1Move(r,c,possible1StartMove,possible1EndMove)
                 valid1Jump(r,c,priority1Start, priority1End)
            elif(grid[r][c] == "b "): #Looks for the kings 
               kingAI1Moves(r, c, possible1StartMove,possible1EndMove)
               king1ValidJump(r,c,priority1Start, priority1End)
               
                 
    if(priority1Start == []): #Moves onto another stack if priorty stack is empty
        if (possible1StartMove == []): #If this stack then
            if(stilPieces() == True): #checks for remianing pieces
                print("Player 2 wins")
                return
            else:
                print("Retry")
                undoKings1() #otherwise, undo the last move
        else:
            selectPiece = random.choice(possible1StartMove) #Randomises the items in the stack
            newPositionIndex = possible1StartMove.index(selectPiece) #grabs the index of the selcted choice
            newPosition  = possible1EndMove[newPositionIndex] #grabs the item at the given index
            
    else:
        selectPiece = random.choice(priority1Start)
        newPositionIndex = priority1Start.index(selectPiece)
        newPosition  = priority1End[newPositionIndex]

    currentMove1.append(selectPiece)
    pastMove1.append(newPosition)
    print("\nCurrent Posirtion: ", selectPiece," New Position: ",newPosition)
        
    toRows  = selectPiece[0]#Converts the sliced string to an int
    toCols  = selectPiece[1]
    newRows = newPosition[0]
    newCols = newPosition[1]    
   
    if(grid[toRows][toCols] == "b "): #if its king do the functions
        kingAI1Oppo(newRows, newCols, toRows ,toCols)
        grid[newRows][newCols] = "b "
    else:
        checkAI1Opponents(newCols,toCols,newRows)
        grid[newRows][newCols] = "B "
        
    checkAI1Status(newRows, newCols)
    grid[toRows][toCols] = "_ "
    
    possible1StartMove.clear() #clears the stack to restart the loop
    possible1EndMove.clear()
    priority1Start.clear()
    priority1End.clear()

def checkIf1Move(r,c,possible1StartMove,possible1EndMove): #simialr to valid move but for the AI
    avaPOSX = r + 1
    avaPOSL = c - 1
    avaPOSR = c + 1
    
    if((avaPOSX < 0 or avaPOSX > 7) or (avaPOSL <-1 or avaPOSL > 7) or (avaPOSR < 0 or avaPOSR > 8)):
        return r, c
    else:
        
        if(c == 0 ): #checks if the column is 0
            if(grid[avaPOSX][avaPOSR]== "_ "):
                possible1StartMove.append((r,c)) #adds the position to the stack
                possible1EndMove.append((avaPOSX, avaPOSR))
                return possible1StartMove, possible1EndMove
            
        elif(c == 7): #checks if the column is 7
             if(grid[avaPOSX][avaPOSL]== "_ "):
                possible1StartMove.append((r,c))
                possible1EndMove.append((avaPOSX, avaPOSL))
                return possible1StartMove, possible1EndMove
            
        elif(c > 0 and c < 7): #checks if the column is between 0 and 7
            if((grid[avaPOSX][avaPOSL] == "_ ") and (grid[avaPOSX][avaPOSR] == "_ ")): #checks if bth postions are free. 
               possible1StartMove.append((r,c))
               possible1EndMove.append((avaPOSX,avaPOSL))
               possible1StartMove.append((r,c))
               possible1EndMove.append((avaPOSX,avaPOSR))
               
            elif (grid[avaPOSX][avaPOSL] == "_ "):
                possible1StartMove.append((r,c))
                possible1EndMove.append((avaPOSX,avaPOSL))
                return possible1StartMove, possible1EndMove

            elif(grid[avaPOSX][avaPOSR]== "_ "):
                possible1StartMove.append((r,c))
                possible1EndMove.append((avaPOSX, avaPOSR))
                return possible1StartMove, possible1EndMove
                    
        if((grid[avaPOSX][avaPOSL] != "_ ") or (grid[avaPOSX][avaPOSR] != "_ ") or (grid[avaPOSX][avaPOSL] == "B ") or (grid[avaPOSX][avaPOSR] == "B ")):
           return

def valid1Jump(r,c,priority1Start, priority1End): #checks if the oppoents are near

    POSX = r + 2 #Looks for an open space either to the left or the right
    POSL = c - 2
    POSR = c + 2

    avaPOSX = r + 1
    avaPOSL = c - 1
    avaPOSR = c + 1
    
                
    if((POSX < -1 or POSX > 7) or (POSL <0 or POSL > 7) or (POSR < 0 or POSR > 7)):
            return
    else:
        if((((grid[POSX][POSR] == "_ ") and (grid[avaPOSX][avaPOSR] == "W ")) or ((grid[POSX][POSR] == "_ ")and(grid[avaPOSX][avaPOSR] == "w "))) #If both ways have oppoent. 
            and (((grid[POSX][POSL] == "_ ") and (grid[avaPOSX][avaPOSL] == "W ")) or (grid[POSX][POSL] == "_ ") and(grid[avaPOSX][avaPOSL] == "W "))):
             priority1Start.append((r,c))#Save both opponents
             priority1End.append((POSX, POSR))
             priority1Start.append((r,c))
             priority1End.append((POSX, POSL))
             return priority1Start, priority1End
            

        elif(grid[POSX][POSR] == "_ "): #if right side has opponents
             if((grid[avaPOSX][avaPOSR] == "W ")or(grid[avaPOSX][avaPOSR] == "w ")):
                 priority1Start.append((r,c))
                 priority1End.append((POSX, POSR))
                 return priority1Start, priority1End
                        
        elif(grid[POSX][POSL] == "_ "):
             if((grid[avaPOSX][avaPOSL] == "W ")or(grid[avaPOSX][avaPOSR] == "w ")): #if left side has opponents
                 priority1Start.append((r,c))
                 priority1End.append((POSX, POSL))
                 return priority1Start, priority1End

def checkAI1Opponents(newCols,toCols,newRows): #simair to the opponents where it overwites thems
    if ((newCols-toCols) == 2):
        #Sqaure moved right 
       a = newRows - 1 #a and b coorindinates for opponent
       b = newCols - 1

       if(grid[a][b] == "W " or grid[a][b] == "w "):
            grid[a][b] = "_ "
            return
            
    if (newCols-toCols == -2): #sqaure moved left
        a = newRows - 1
        b = newCols + 1
        if(grid[a][b] == "W " or grid[a][b] == "w "):
            grid[a][b] = "_ "
            return
      
    return

def checkAI1Status(newRows, newCols): #AIs check of its a king 

    if(newRows == 7):
        grid[newRows][newCols] = "b "
        return
    else:
        return False

def kingAI1Moves(r,c, possible1StartMove,possible1EndMove): #simiar to the moves but for kings

    avaPOSX = r + 1
    avaPOSL = c - 1
    avaPOSR = c + 1
    avaPOSY = r - 1

    if((avaPOSX < 0 or avaPOSX > 8) or (avaPOSL <-1 or avaPOSL > 7) or (avaPOSR < 0 or avaPOSR > 7)):
        return r, c
    else:
        if (r == 7): #checks if the row is 7 then move down
            if(c == 0 ):
                 if(grid[avaPOSY][avaPOSR]== "_ "):
                    possible1StartMove.append((r,c))
                    possible1EndMove.append((avaPOSY, avaPOSR))
                    return priority1Start, priority1End
                    
            elif(c == 7):
                 if(grid[avaPOSY][avaPOSL]== "_ "):
                    possible1StartMove.append((r,c))
                    possible1EndMove.append((avaPOSY, avaPOSL))
                    return priority1Start, priority1End
                    
            elif(c > 0 and c < 7):
                if((grid[avaPOSY][avaPOSL] == "_ ") and (grid[avaPOSY][avaPOSR] == "_ ")):
                   possible1StartMove.append((r,c))
                   possible1EndMove.append((avaPOSY,avaPOSL))
                   possible1StartMove.append((r,c))
                   possible1EndMove.append((avaPOSY,avaPOSR))
                   return possible1StartMove, possible1EndMove
               
                elif (grid[avaPOSY][avaPOSL] == "_ "):
                    possible1StartMove.append((r,c))
                    possible1EndMove.append((avaPOSY,avaPOSL))
                    return priority1Start, priority1End
                    

                elif(grid[avaPOSY][avaPOSR]== "_ "):
                    possible1StartMove.append((r,c))
                    possible1EndMove.append((avaPOSY, avaPOSR))
                    return priority1Start, priority1End
                    
            if((grid[avaPOSY][avaPOSL] != "_ ") or (grid[avaPOSY][avaPOSR] != "_ ") or (grid[avaPOSY][avaPOSL] == "W ") or (grid[avaPOSY][avaPOSR] == "W ")):
              return
            
        elif (r > 0 and r < 7): #checks if the row is between 0 and 7 then move 
            
            if(c == 0 ):               
                if(grid[avaPOSY][avaPOSR]== "_ "):
                    possible1StartMove.append((r,c))
                    possible1EndMove.append((avaPOSY, avaPOSR))
                    return priority1Start, priority1End
                    
                
               
                
            elif(c == 7):                
                if(grid[avaPOSY][avaPOSL]== "_ "):
                    possible1StartMove.append((r,c))
                    possible1EndMove.append((avaPOSY, avaPOSL))
                    return priority1Start, priority1End
                    
                
                
            elif(c > 0 and c < 7):              
                if(grid[avaPOSX][avaPOSR]== "_ "):
                    possible1StartMove.append((r,c))
                    possible1EndMove.append((avaPOSX, avaPOSR))
                    return possible1StartMove, possible1EndMove
                    

                if((grid[avaPOSY][avaPOSL] == "_ ") and (grid[avaPOSY][avaPOSR] == "_ ")):
                   possible1StartMove.append((r,c))
                   possible1EndMove.append((avaPOSY,avaPOSL))
                   possible1StartMove.append((r,c))
                   possible1EndMove.append((avaPOSY,avaPOSR))
                   return priority1Start, priority1End
                    
               
                elif (grid[avaPOSY][avaPOSL] == "_ "):
                    possible1StartMove.append((r,c))
                    possible1EndMove.append((avaPOSY,avaPOSL))
                    return priority1Start, priority1End

                elif(grid[avaPOSY][avaPOSR]== "_ "):
                    possible1StartMove.append((r,c))
                    possible1EndMove.append((avaPOSY, avaPOSR))
                    return priority1Start, priority1End
            
            if((grid[avaPOSX][avaPOSL] != "_ ") or (grid[avaPOSX][avaPOSR] != "_ ") or (grid[avaPOSX][avaPOSL] == "W ") or (grid[avaPOSX][avaPOSR] == "W ") or
               (grid[avaPOSY][avaPOSL] != "_ ") or (grid[avaPOSY][avaPOSR] != "_ ") or (grid[avaPOSY][avaPOSL] == "W ") or (grid[avaPOSY][avaPOSR] == "W ")):
              return

        elif (r == 0): #checks if the row is 0 then move up
            
            if(c == 0 ):
                if(grid[avaPOSX][avaPOSR]== "_ "):
                    possible1StartMove.append((r,c))
                    possible1EndMove.append((avaPOSX, avaPOSR))
                    return possible1StartMove, possible1EndMove                
                   
                
            elif(c == 7):
                if(grid[avaPOSX][avaPOSL]== "_ "):
                    possible1StartMove.append((r,c))
                    possible1EndMove.append((avaPOSX, avaPOSL))
                    return possible1StartMove, possible1EndMove
                    
                
            elif(c > 0 and c < 7):

                if(grid[avaPOSX][avaPOSR]== "_ "):
                    possible1StartMove.append((r,c))
                    possible1EndMove.append((avaPOSX, avaPOSR))
                    return possible1StartMove, possible1EndMove     
            
    return grid
def king1ValidJump(r,c,priority1Start, priority1End):

    POSX = r + 2 #Looks for an open space either to the left or the right
    POSL = c - 2
    POSR = c + 2
    POSY = r - 2

    avaPOSX = r + 1
    avaPOSL = c - 1
    avaPOSR = c + 1
    avaPOSY = r - 1
    
    if((POSX < 0 or POSX > 7) or (POSL <0 or POSL > 7) or (POSR < 0 or POSR > 7)):
            return
    else:
        if((((grid[POSX][POSR] == "_ ") and (grid[avaPOSX][avaPOSR] == "W ")) or ((grid[POSX][POSR] == "_ ")and(grid[avaPOSX][avaPOSR] == "w ")))
            and (((grid[POSX][POSL] == "_ ") and (grid[avaPOSX][avaPOSL] == "W ")) or (grid[POSX][POSL] == "_ ") and(grid[avaPOSX][avaPOSL] == "W "))):
             priority1Start.append((r,c))
             priority1End.append((POSX, POSR))
             priority1Start.append((r,c))
             priority1End.append((POSX, POSL))
             return priority1Start, priority1End
            

        elif(grid[POSX][POSR] == "_ "):
             if(grid[avaPOSX][avaPOSR] == "W " or grid[avaPOSX][avaPOSR] == "w "):
                 priority1Start.append((r,c))
                 priority1End.append((POSX, POSR))
                 return priority1Start, priority1End
                        
        elif(grid[POSX][POSL] == "_ "):
             if(grid[avaPOSX][avaPOSL] == "W " or grid[avaPOSX][avaPOSL] == "w "):
                 priority1Start.append((r,c))
                 priority1End.append((POSX, POSL))
                 return priority1Start, priority1End
                
        if((((grid[POSY][POSR] == "_ ") and (grid[avaPOSY][avaPOSR] == "W ")) or ((grid[POSY][POSR] == "_ ")and(grid[avaPOSY][avaPOSR] == "w ")))
            and (((grid[POSY][POSL] == "_ ") and (grid[avaPOSY][avaPOSL] == "W ")) or (grid[POSY][POSL] == "_ ") and(grid[avaPOSY][avaPOSL] == "W "))):
             priority1Start.append((r,c))
             priority1End.append((POSY, POSR))
             priority1Start.append((r,c))
             priority1End.append((POSY, POSL))
             return priority1Start, priority1End
            

        elif(grid[POSY][POSR] == "_ "):
             if(grid[avaPOSY][avaPOSR] == "W " or grid[avaPOSY][avaPOSR] == "w "):
                 priority1Start.append((r,c))
                 priority1End.append((POSY, POSR))
                 return priority1Start, priority1End
                        
        elif(grid[POSY][POSL] == "_ "):
             if(grid[avaPOSY][avaPOSL] == "W " or grid[avaPOSY][avaPOSL] == "w "):
                 priority1Start.append((r,c))
                 priority1End.append((POSY, POSL))
                 return priority1Start, priority1End

def kingAI1Oppo(newRows, newCols, toRows ,toCols):
    if ((newRows - toCols) == 2):  #Sqaure moves right 
        if((newRows - toRows) == 2): #sqaure moved down
           
            a = newRows - 1 #a and b coorindinates for opponent
            b = newCols - 1 
            if(grid[a][b] == "W " or grid[a][b] == "w "):
                grid[a][b] = "_ "
                
        elif((newRows-toRows)== -2): #sqaure moved up
            a = newPOSX + 1 #a and b coorindinates for opponent
            b = newPOSY - 1
           
            if(grid[a][b] == "W " or grid[a][b] == "w "):
                grid[a][b] = "_ "   
        
            
    if (newCols-toCols == -2): #sqaure moved left
         if((newRows - toRows) == 2): #sqaure moved down
           
            a = newRows - 1 #a and b coorindinates for opponent
            b = newCols + 1
            if(grid[a][b] == "W " or grid[a][b] == "w "):
                grid[a][b] = "_ "
                
         elif((newRows-toRows)== -2): #sqaure moved up
            a = newRows + 1 #a and b coorindinates for opponent
            b = newCols + 1
            
            if(grid[a][b] == "W " or grid[a][b] == "w "):
                grid[a][b] = "_ "

def AIMoves(j):
    stilPieces()
    print("Player 2")
    draw_grid(grid)
    for r in range(height):
        for c in range(width):
            if(grid[r][c] == "W "):
                 checkIfMove(r,c,possibleStartMove,possibleEndMove)
                 validJump(r,c,priorityStart, priorityEnd)
            elif (grid[r][c] == "w "):
                kingAIMoves(r,c)
                kingValidJump(r,c,priorityStart, priorityEnd)
                 
    if(priorityStart == []):
        if (possibleStartMove == []):
            if(stilPieces()== True):
                print("Player 1 wins")
                return
            else:
                undoKings((toRows,toCols,newRows,newCols))
                print("Retry")
        else:
            selectPiece = random.choice(possibleStartMove)
            newPositionIndex = possibleStartMove.index(selectPiece)
            newPosition  = possibleEndMove[newPositionIndex]
        
    else:
        selectPiece = random.choice(priorityStart)
        newPositionIndex = priorityStart.index(selectPiece)
        newPosition  = priorityEnd[newPositionIndex]
    currentMove2.append(selectPiece)
    pastMove2.append(newPosition)
    print("\nCurrent Posirtion: ", selectPiece," New Position: ",newPosition)
    
    toRows  = selectPiece[0]#Converts the sliced string to an int
    toCols  = selectPiece[1]
    newRows = newPosition[0]
    newCols = newPosition[1]

    if(grid[toRows][toCols] == "w "):
        kingAIOppo(newRows, newCols, toRows ,toCols)
        grid[newRows][newCols] = "w "
    else:
        checkAIOpponents(newCols,toCols,newRows)
        grid[newRows][newCols] = "W "

    checkAIStatus(newRows, newCols)
    grid[toRows][toCols] = "_ "
    
    possibleStartMove.clear()
    possibleEndMove.clear()
    priorityStart.clear()
    priorityEnd.clear()

def checkIfMove(r,c,possibleStartMove,possibleEndMove):
    avaPOSX = r - 1
    avaPOSL = c - 1
    avaPOSR = c + 1
    
    if((avaPOSX < -1 or avaPOSX > 7) or (avaPOSL <-1 or avaPOSL > 7) or (avaPOSR < 0 or avaPOSR > 8)):
        return r, c
    else:
        
        if(c == 0 ):
            if(grid[avaPOSX][avaPOSR]== "_ "):
                possibleStartMove.append((r,c))
                possibleEndMove.append((avaPOSX, avaPOSR))
                return possibleStartMove, possibleEndMove
            
        elif(c == 7):
             if(grid[avaPOSX][avaPOSL]== "_ "):
                possibleStartMove.append((r,c))
                possibleEndMove.append((avaPOSX, avaPOSL))
                return possibleStartMove, possibleEndMove
        elif(c > 0 and c < 7):
            if((grid[avaPOSX][avaPOSL] == "_ ") and (grid[avaPOSX][avaPOSR] == "_ ")):
               possibleStartMove.append((r,c))
               possibleEndMove.append((avaPOSX,avaPOSL))
               possibleStartMove.append((r,c))
               possibleEndMove.append((avaPOSX,avaPOSR))
               
            elif (grid[avaPOSX][avaPOSL] == "_ "):
                possibleStartMove.append((r,c))
                possibleEndMove.append((avaPOSX,avaPOSL))
                return possibleStartMove, possibleEndMove

            elif(grid[avaPOSX][avaPOSR]== "_ "):
                possibleStartMove.append((r,c))
                possibleEndMove.append((avaPOSX, avaPOSR))
                return possibleStartMove, possibleEndMove
                    
        if((grid[avaPOSX][avaPOSL] != "_ ") or (grid[avaPOSX][avaPOSR] != "_ ") or (grid[avaPOSX][avaPOSL] == "W ") or (grid[avaPOSX][avaPOSR] == "W ")):
           return

def validJump(r,c,priorityStart, priorityEnd):

    POSX = r - 2 #Looks for an open space either to the left or the right
    POSL = c - 2
    POSR = c + 2

    avaPOSX = r - 1
    avaPOSL = c - 1
    avaPOSR = c + 1
    
    
    if((POSX < 0 or POSX > 7) or (POSL <0 or POSL > 7) or (POSR < 0 or POSR > 7)):
            return
    else:
        if((((grid[POSX][POSR] == "_ ") and (grid[avaPOSX][avaPOSR] == "B ")) or ((grid[POSX][POSR] == "_ ")and(grid[avaPOSX][avaPOSR] == "b ")))
            and (((grid[POSX][POSL] == "_ ") and (grid[avaPOSX][avaPOSL] == "B ")) or (grid[POSX][POSL] == "_ ") and(grid[avaPOSX][avaPOSL] == "b "))):
             priorityStart.append((r,c))
             priorityEnd.append((POSX, POSR))
             priorityStart.append((r,c))
             priorityEnd.append((POSX, POSL))
             return priorityStart, priorityEnd
            

        elif(grid[POSX][POSR] == "_ "):
             if(grid[avaPOSX][avaPOSR] == "B "):
                 priorityStart.append((r,c))
                 priorityEnd.append((POSX, POSR))
                 return priorityStart, priorityEnd
                        
        elif(grid[POSX][POSL] == "_ "):
             if(grid[avaPOSX][avaPOSL] == "B "):
                 priorityStart.append((r,c))
                 priorityEnd.append((POSX, POSL))
                 return priorityStart, priorityEnd

def checkAIOpponents(newCols,toCols,newRows):
    if ((newCols-toCols) == 2):
        #Sqaure moved right 
        a = newRows + 1 #a and b coorindinates for opponent
        b = newCols - 1
        
        if(grid[a][b] == "B " or grid[a][b] == "b "):
            grid[a][b] = "_ "
            return
            
    if (newCols-toCols == -2): #sqaure moved left
        a = newRows + 1
        b = newCols + 1
        if(grid[a][b] == "B " or grid[a][b] == "b "):
            grid[a][b] = "_ "
            return
    return

def checkAIStatus(newRows, newCols):

    if(newRows == 0):
        grid[newRows][newCols] = "w "
    else:
        return False

def kingAIMoves(r,c):
    avaPOSX = r - 1
    avaPOSL = c - 1
    avaPOSR = c + 1
    avaPOSY = r + 1
    
    if((avaPOSX < -1 or avaPOSX > 7) or (avaPOSL <-1 or avaPOSL > 7) or (avaPOSR < 0 or avaPOSR > 7) or (avaPOSY < -1 or avaPOSY > 7)):
        return r, c
    else:
       if(r == 0):
            if(c == 0 ):
                 if(grid[avaPOSY][avaPOSR]== "_ "):
                    possibleStartMove.append((r,c))
                    possibleEndMove.append((avaPOSY, avaPOSR))
                    return priorityStart, priorityEnd
            
            elif(c == 7):
                 if(grid[avaPOSY][avaPOSL]== "_ "):
                    possibleStartMove.append((r,c))
                    possibleEndMove.append((avaPOSY, avaPOSL))
                    return priorityStart, priorityEnd
                
            elif(c > 0 and c < 7):
                if((grid[avaPOSY][avaPOSL] == "_ ") and (grid[avaPOSY][avaPOSR] == "_ ")):
                   possibleStartMove.append((r,c))
                   possibleEndMove.append((avaPOSY,avaPOSL))
                   possibleStartMove.append((r,c))
                   possibleEndMove.append((avaPOSY,avaPOSR))
                   return priorityStart, priorityEnd
               
                elif (grid[avaPOSY][avaPOSL] == "_ "):
                    possibleStartMove.append((r,c))
                    possibleEndMove.append((avaPOSY,avaPOSL))
                    return priorityStart, priorityEnd

                elif(grid[avaPOSY][avaPOSR]== "_ "):
                    possibleStartMove.append((r,c))
                    possibleEndMove.append((avaPOSY, avaPOSR))
                    return priorityStart, priorityEnd
                
                if((grid[avaPOSY][avaPOSL] != "_ ") or (grid[avaPOSY][avaPOSR] != "_ ") or (grid[avaPOSY][avaPOSL] == "W ") or (grid[avaPOSY][avaPOSR] == "W ")):
                  return
            
       elif (r > 0 and r < 8):
            if(c == 0 ):
                if(grid[avaPOSY][avaPOSR]== "_ "):
                    possibleStartMove.append((r,c))
                    possibleEndMove.append((avaPOSY, avaPOSR))
                    return priorityStart, priorityEnd
                
               
                
            elif(c == 7):                
                if(grid[avaPOSY][avaPOSL]== "_ "):
                    possibleStartMove.append((r,c))
                    possibleEndMove.append((avaPOSY, avaPOSL))
                    return priorityStart, priorityEnd
                
                
            elif(c > 0 and c < 7):     
                if (grid[avaPOSX][avaPOSL] == "_ "):
                    possibleStartMove.append((r,c))
                    possibleEndMove.append((avaPOSX,avaPOSL))
                    return possibleStartMove, possibleEndMove

                if((grid[avaPOSY][avaPOSL] == "_ ") and (grid[avaPOSY][avaPOSR] == "_ ")):
                   possibleStartMove.append((r,c))
                   possibleEndMove.append((avaPOSY,avaPOSL))
                   possibleStartMove.append((r,c))
                   possibleEndMove.append((avaPOSY,avaPOSR))
                   return priorityStart, priorityEnd
               
                elif (grid[avaPOSY][avaPOSL] == "_ "):
                    possibleStartMove.append((r,c))
                    possibleEndMove.append((avaPOSY,avaPOSL))
                    return priorityStart, priorityEnd
                
                elif(grid[avaPOSY][avaPOSR]== "_ "):
                    possibleStartMove.append((r,c))
                    possibleEndMove.append((avaPOSY, avaPOSR))
                    return priorityStart, priorityEnd
            
                if((grid[avaPOSX][avaPOSL] != "_ ") or (grid[avaPOSX][avaPOSR] != "_ ") or (grid[avaPOSX][avaPOSL] == "W ") or (grid[avaPOSX][avaPOSR] == "W ") or
                   (grid[avaPOSX][avaPOSL] == "w ") or (grid[avaPOSX][avaPOSR] == "w ")or (grid[avaPOSY][avaPOSL] != "_ ") or (grid[avaPOSY][avaPOSR] != "_ ") or
                   (grid[avaPOSY][avaPOSL] == "W ") or (grid[avaPOSY][avaPOSR] == "W ")or(grid[avaPOSY][avaPOSL] == "w ") or (grid[avaPOSY][avaPOSR] == "w ")):
                  return

            if(r == 7):
                if(c == 0 ):
                    if(grid[avaPOSX][avaPOSR]== "_ "):
                        possibleStartMove.append((r,c))
                        possibleEndMove.append((avaPOSX, avaPOSR))
                        return possibleStartMove, possibleEndMove
            
                    elif(c == 7):
                         if(grid[avaPOSX][avaPOSL]== "_ "):
                            possibleStartMove.append((r,c))
                            possibleEndMove.append((avaPOSX, avaPOSL))
                            return possibleStartMove, possibleEndMove
                        
                    elif(c > 0 and c < 7):
                        if(grid[avaPOSX][avaPOSR]== "_ "):
                            possibleStartMove.append((r,c))
                            possibleEndMove.append((avaPOSX, avaPOSR))
                            return possibleStartMove, possibleEndMove    
        
    
    return grid
def kingValidJump(r,c,riorityStart, priorityEnd):

    POSX = r - 2 #Looks for an open space either to the left or the right
    POSL = c - 2
    POSR = c + 2
    POSY = r + 2

    avaPOSX = r - 1
    avaPOSL = c - 1
    avaPOSR = c + 1
    avaPOSY = r + 1
    
    if((POSX < 0 or POSX > 7) or (POSL <0 or POSL > 7) or (POSR < 0 or POSR > 7) or (avaPOSY < -1 or avaPOSY > 7)):
            return
    else:
        if((((grid[POSX][POSR] == "_ ") and (grid[avaPOSX][avaPOSR] == "B ")) or ((grid[POSX][POSR] == "_ ")and(grid[avaPOSX][avaPOSR] == "b ")))
            and (((grid[POSX][POSL] == "_ ") and (grid[avaPOSX][avaPOSL] == "B ")) or (grid[POSX][POSL] == "_ ") and(grid[avaPOSX][avaPOSL] == "b "))):

             priorityStart.append((r,c))
             priorityEnd.append((POSX, POSR))
             priorityStart.append((r,c))
             priorityEnd.append((POSX, POSL))
             return priorityStart, priorityEnd
            

        elif(grid[POSX][POSR] == "_ "):
             if((grid[avaPOSX][avaPOSR] == "B " ) or (grid[avaPOSX][avaPOSR] == "b ")):
                 priorityStart.append((r,c))
                 priorityEnd.append((POSX, POSR))
                 return priorityStart, priorityEnd
                        
        elif(grid[POSX][POSL] == "_ "):
             if((grid[avaPOSX][avaPOSL] == "B ")or(grid[avaPOSX][avaPOSL] == "b ")):
                 priorityStart.append((r,c))
                 priorityEnd.append((POSX, POSL))
                 return priorityStart, priorityEnd
                
        if((((grid[POSY][POSR] == "_ ") and (grid[avaPOSY][avaPOSR] == "B ")) or ((grid[POSY][POSR] == "_ ") and(grid[avaPOSY][avaPOSR] == "b ")))
            and (((grid[POSY][POSL] == "_ ") and (grid[avaPOSY][avaPOSL] == "B ")) or (grid[POSY][POSL] == "_ ") and(grid[avaPOSY][avaPOSL] == "b "))):
             priorityStart.append((r,c))
             priorityEnd.append((POSY, POSR))
             priorityStart.append((r,c))
             priorityEnd.append((POSY, POSL))
             return priorityStart, priorityEnd
            

        elif(grid[POSX][POSR] == "_ "):
             if((grid[avaPOSY][avaPOSR] == "B ")or(grid[avaPOSY][avaPOSR] == "b ")):
                 priorityStart.append((r,c))
                 priorityEnd.append((POSY, POSR))
                 return priorityStart, priorityEnd
                        
        elif(grid[POSX][POSL] == "_ "):
             if((grid[avaPOSY][avaPOSL] == "B ") or (grid[avaPOSY][avaPOSL] == "b ")):
                 priorityStart.append((r,c))
                 priorityEnd.append((POSY, POSL))
                 return priorityStart, priorityEnd

def kingAIOppo(newRows, newCols, toRows ,toCols):
    if ((newCols - toCols) == 2):  #Sqaure moves right 
        if((newRows - toRows) == 2): #sqaure moved down
           
            a = newRows - 1 #a and b coorindinates for opponent
            b = newCols - 1 
            if(grid[a][b] == "B " or grid[a][b] == "b "):
                grid[a][b] = "_ "
                
        elif((newRows-toRows)== -2): #sqaure moved up
            a = newRows + 1 #a and b coorindinates for opponent
            b = newCols - 1
           
            if(grid[a][b] == "B " or grid[a][b] == "b "):
                grid[a][b] = "_ "    
        
            
    if (newCols-toCols == -2): #sqaure moved left
         if((newRows - toRows) == 2): #sqaure moved down
           
            a = newRows - 1 #a and b coorindinates for opponent
            b = newCols + 1
            if(grid[a][b] == "B " or grid[a][b] == "b "):
                grid[a][b] = "_ "
                
         elif((newRows-toRows)== -2): #sqaure moved up
            a = newCols + 1 #a and b coorindinates for opponent
            b = newRows + 1
            
            if(grid[a][b] == "B " or grid[a][b] == "b "):
                grid[a][b] = "_ "


    
def undo_feature(i,pastMove1,currentMove1,redoFeaturePOS1,redoFeaturePOS2): #undo feature for player1
    i-=1
    toRows  = int (currentMove1[i][0:1]) #Converts the sliced string to an int
    toCols  = int (currentMove1[i][2:3])
  
    newPOSX  = int (pastMove1[i][0:1]) #temp coordinates
    newPOSY  = int (pastMove1[i][2:3])
    if(newPOSY - toCols == 2 or newPOSY - toCols == - 2):
        print("Cannot undo an opponent")
        return secondMoves(j)
    else:
        print("Undo Selected")
        redoFeaturePOS1.append(currentMove1[i]) #saves them to a temp file
        redoFeaturePOS2.append(pastMove1[i])
        currentMove1.pop() #removes the last item in the stack
        pastMove1.pop()

        if (grid[toRows][toCols] == "_ "):
               
                grid[newPOSX][newPOSY] = "_ "  #changes the avilabe space to B and the last space to _
                grid[toRows][toCols] = "B "
               
                print(i)
                print("Move Deleted")
                return firstMove(i), secondMoves(j)  

def undo_feature_2(j,pastMove2,currentMove2,redoFeature2POS1,redoFeature2POS2): #undo feature for Player 2
    j-=1
    toRows  = int (currentMove2[j][0:1]) #Converts the sliced string to an int
    toCols  = int (currentMove2[j][2:3])
  
    newPOSX  = int (pastMove2[j][0:1]) #temp coordinates
    newPOSY  = int (pastMove2[j][2:3])
    if(newPOSY - toCols == 2 or newPOSY - toCols == - 2):
        print("Cannot undo an opponent")
        return firstMove(i)
    else:
        print("Undo Selected")
        redoFeature2POS1.append(currentMove2[j])
        redoFeature2POS2.append(pastMove2[j])
        print(pastMove2)
        currentMove2.pop()
        pastMove2.pop()

        if (grid[toRows][toCols] == "_ "):
               
                grid[newPOSX][newPOSY] = "_ "  #changes the avilabe space to B and the last space to _
                grid[toRows][toCols] = "W "
                print("Move Deleted")
                return secondMoves(j), firstMove(i)

def redoFeature(i, pastMove1, currentMove1): #redo feature for Player 1
    print("Redo  Selected")
    currentMove1.append(redoFeaturePOS1[i]) #saves the temp file to the new stack
    pastMove1.append(redoFeaturePOS2[i])
    currentMove1.pop()
    pastMove1.pop()
    toRows  = int (redoFeaturePOS1[i][0:1]) #Converts the sliced string to an int
    toCols  = int (redoFeaturePOS1[i][2:3])
  
    newPOSX  = int (redoFeaturePOS2[i][0:1]) #temp coordinates
    newPOSY  = int (redoFeaturePOS2[i][2:3])
  
    if (grid[toRows][toCols] == "B "):
           
            grid[newPOSX][newPOSY] = "B "  #changes the avilabe space to B and the last space to _
            grid[toRows][toCols] = "_ "
           
            print("Move Changed")
            return secondMoves(j), firstMove(i), redoFeaturePOS1, redoFeaturePOS2

def redo_feature2(j, pastMove2, currentMove2): # redo feature for Player 2
    print("Redo  Selected")
    print(j)

    currentMove2.append(redoFeature2POS1[j])
    pastMove2.append(redoFeature2POS2[j])
    currentMove2.pop()
    pastMove2.pop()
    toRows  = int (redoFeature2POS1[j][0:1]) #Converts the sliced string to an int
    toCols  = int (redoFeature2POS1[j][2:3])
  
    newPOSX  = int (redoFeature2POS2[j][0:1]) #temp coordinates
    newPOSY  = int (redoFeature2POS2[j][2:3])
  
    if (grid[toRows][toCols] == "W "):
           
            grid[newPOSX][newPOSY] = "W "  #changes the avilabe space to B and the last space to _
            grid[toRows][toCols] = "_ "
           
            print(j)
            print("Move Changed")
            return firstMove(i),secondMoves(j), redoFeature2POS1, redoFeature2POS2

def undoKings(): #undo feature for AI Player 2
    currentMove2.pop()
    pastMove2.pop()
    toRows  = int (currentMove2[j][0:1]) #Converts the sliced string to an int
    toCols  = int (currentMove2[j][2:3])
  
    newRows  = int (pastMove2[j][0:1]) #temp coordinates
    newCols  = int (pastMove2[j][2:3])
    return AIMoves(j), AI1Moves(i)

def undoKings1(): #undo feature for AI Player 1
    currentMove1.pop()
    pastMove1.pop()
    toRows  = int (currentMove1[i][0:1]) #Converts the sliced string to an int
    toCols  = int (currentMove1[i][2:3])
  
    newRows  = int (pastMove1[i][0:1]) #temp coordinates
    newCols  = int (pastMove1[i][2:3])
    return AI1Moves(i),AIMoves(j)


def replayFeature(i,pastMove1,currentMove1,a,b): #Replay feature for Player 1
     replay = input("Would you like to Replay that move? Y/N")
     if(replay == "Y"):
         toRows  = int (currentMove1[i][0:1]) #Converts the sliced string to an int
         toCols  = int (currentMove1[i][2:3])
         newPOSX  = int (pastMove1[i][0:1]) #temp coordinates
         newPOSY  = int (pastMove1[i][2:3])
         print("\nBEFORE")
         if (grid[toRows][toCols] == "_ "):
             grid[newPOSX][newPOSY] = "_ "  #changes the avilabe space to B and the last space to _
             grid[toRows][toCols] = "B "
             grid[a][b] = "W " 
         draw_grid(grid)
         
         print("\nAFTER")
         if (grid[toRows][toCols] == "B "):
              grid[newPOSX][newPOSY] = "B "  #changes the avilabe space to B and the last space to _
              grid[toRows][toCols] = "_ "
              grid[a][b] = "_ "
         draw_grid(grid)
         return    
     elif(replay == "N"):
         return

         


def replayFeature2(j,currentMove2,pastMove2,a,b): #Replay feature for Player 2
    replay = input("Would you like to Replay that move? Y/N")
    if(replay == "Y"):
         toRows  = int (currentMove2[j][0:1]) #Converts the sliced string to an int
         toCols  = int (currentMove2[j][2:3])
         newPOSX = int (pastMove2[j][0:1]) #temp coordinates
         newPOSY = int (pastMove2[j][2:3])

         print("\nBEFORE")
         if (grid[toRows][toCols] == "_ "):
             grid[newPOSX][newPOSY] = "_ "  #changes the avilabe space to B and the last space to _
             grid[toRows][toCols] = "W "
             grid[a][b] = "B " 
         draw_grid(grid)
         
         print("\nAFTER")
         if (grid[toRows][toCols] == "W "):
              grid[newPOSX][newPOSY] = "W "  #changes the avilabe space to B and the last space to _
              grid[toRows][toCols] = "_ "
              grid[a][b] = "_ "
         draw_grid(grid)
         return    
    elif(replay == "N"):
         return
     
    
    
          
##Global Variables
width = 8
height = 8

pastMove1=[]
pastMove2=[]
currentMove1=[]
currentMove2=[]
redoFeaturePOS1 = []
redoFeaturePOS2 = []
redoFeature2POS1 =[]
redoFeature2POS2 =[]

possibleStartMove =[]
possibleEndMove =[]
priorityStart = []
priorityEnd = []
possible1StartMove =[]
possible1EndMove =[]
priority1Start = []
priority1End = []


i = 0
j = 0                      

                       
#Main Program
instruction()
opponent = input("Select your opponent \n1. Human vs Human\n2. Human vs Computer \n3. Computer Vs Computer") #Allows the user to select their opponent.
while((opponent != '1') or (opponent != '2') or (opponent != '3')):
    if(opponent == '1'): 
        print("You have selected Human vs Human")
        grid = init_board()
        while(stilPieces() == False):
            firstMove(i)
            i+=1
            secondMoves(j)
            j+=1

        print("Game Ended")
        
    elif(opponent == '2'):
       

        print("You have selected Humann vs Computer")
        grid = init_board()
        while(stilPieces() == 0):
            firstMove(i)
            i+=1
            AIMoves(j)
            j+=1
       
        print("Game Ended")
            
    

    elif(opponent == '3'):
        print("You have selected Computer vs Computer")
        grid = init_board()
        while(stilPieces() == False):

            AI1Moves(i)
            i+=1
            nextMove = input("Press n to view Next Move.")
            if(nextMove == "n"):
                AIMoves(j)
                j+=1
                nextMove1 = input("Press n to view Next Move.")
                while(nextMove1 != "n"):
                    if(nextMove != "n"):
                        nextMove1 = input("Press n to view Next Move.")
                    else:
                        break                    
            elif(nextMove != "n"):
                 nextMove = input("Press n to view Next Move.")
                
                    
        print("Game Ended")
            
    if((opponent != '1') or (opponent != '2') (opponent != '3')):
        opponent = input("Select your opponent \n1. Human vs Computer\n2. Humnan vs Human \n3. Computer Vs Computer")
