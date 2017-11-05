import random
def instruction():
    print("Welcome to a game of draughts. Player 1. Select your Opponent. You have a choice of two. Agaisnt your frind or Play agasint the computer")
    print("Rules:")
    print("     1. The format of the cordinates is 0.0")
    print("     2. Each will take turn to move")
    print("     3. The game will end when someone has no pieces left")
    print("     4. Double jumping is NOT allowed")
    print("     5. Pieces are only allowed to move 1 spot at a time only if they are stealing an opponents piece")
    print("     6. To undo a move, write 'undo' on your opponents\ns")
    print("     7. Player 1 = 'B' & Player 2 = 'W' ")
    print("     8. Kings will be changed to 'b' & 'w'\n")


def init_board(): #Intializes the board :
    grid = [[0 for x in range(width)] for y in range(height)] # creates the list 

    for x in range(width):
        print("")
        for y in range(height):
            if(x <3 and (y%2)!=0): #Sets the board for the Black characters
                if((x%2)== 0):
                    grid[x][y] = "B "
                else:
                    grid[x][y] = "| "
            elif (x <3 and (y%2)==0):
                if((x%2)!= 0):
                    grid[x][y] = "B "
                else:
                    grid[x][y] = "| "

            if((x >2 and x <5) and ((y%2)!=0)):
                if((x%2)== 0):
                    grid[x][y] = "_ "
                else:
                    grid[x][y] = "| "
            elif ((x >2 and x <5) and (y%2)==0):
                if((x%2)!= 0):
                    grid[x][y] = "_ "
                else:
                    grid[x][y] = "| "
                
            
            
            if(x >4 and (y%2)!=0):
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

def stilPieces(bool):
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

    if(countB > 1 or countW > 1):
        return False
    elif(countB == 0 or countW ==0 ):
            
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
            
    currentMove1.append(input("Select piece to move"))
    if(currentMove1[i] == "undo"):
        currentMove1.pop()
        undo_feature_2(j,pastMove2,currentMove2)
    else:
        validPOS1(currentMove1, pastMove1,i) #Another Function
        stilPieces(bool)

    return grid

def validPOS1(currentMove1,pastMove1,i):
    toRows  = int (currentMove1[i][0:1]) #Converts the sliced string to an int
    toCols  = int (currentMove1[i][2:3])

    avaPOSX = toRows + 1 #chnages the coordinates to llok for the avaliable spaces near by
    avaPOSL = toCols - 1
    avaPOSR = toCols + 1

    POSX = toRows + 2
    POSL = toCols - 2
    POSR = toCols + 2


    if(grid[toRows][toCols] == "b "):
    
        kingMoves(toRows, toCols,i, pastMove1,currentMove1)
    else:
        
        response = False
        
        if((toRows < 0 or toRows >7) or (toCols < 0 or toCols > 7)): #checks if the input is in range
            if((avaPOSX <0 or avaPOSX > 7) or (avaPOSL <0 or avaPOSL >7) or (avaPOSR <0 and avaPOSR >7)):#checka whether the avalaible pos are in range
                print("Out of Range")
                currentMove1.append(input("Select piece to move"))
                toRows  = int (currentMove1[i][0:1]) #Converts the sliced string to an int
                toCols  = int (currentMove1[i][2:3])

                avaPOSX = toRows + 1
                avaPOSL = toCols - 1
                avaPOSR = toCols + 1
                
                
            else:
                while(((grid[avaPOSX][avaPOSL] != "_ ") or (grid[avaPOSX][avaPOSR] != "_ ") or (grid[POSX][POSR] != "_ ")
                       or( grid[POSX][POSL] != "_ "))  and response == False):

                    if (grid[avaPOSX][avaPOSL] == "_ " ): #if the ava POS has a space
                        response = True

                    if (grid[POSX][POSL] == "_ " ): # check if there was a free spot 2 spaces away and then checks if pplayer 2 is a spot away. 
                        if(grid[avaPOSX][avaPOSL] == "W " or grid[avaPOSX][avaPOSR] == "w "): 
                            response = True
                
                    elif (grid[avaPOSX][avaPOSR] == "_ "): 
                        response = True
               
                
                    elif(grid[POSX][POSR] == "_ "):
                        if(grid[avaPOSX][avaPOSR] == "W " or grid[avaPOSX][avaPOSR] == "w " ):
                            response = True
                        
                    
                    if((grid[avaPOSX][avaPOSL] != "_ ") and (grid[avaPOSX][avaPOSR] != "_ ") and (grid[POSX][POSR] != "_ ") and (grid[POSX][POSL] != "_ ")):
                            currentMove1.append(input("Select piece to move"))
                            toRows  = int (currentMove1[i][0:1]) #Converts the sliced string to an int
                            toCols  = int (currentMove1[i][2:3])
                            avaPOSX = toRows + 1 #chnages the coordinates to llok for the avaliable spaces near by
                            avaPOSL = toCols - 1
                            avaPOSR = toCols + 1
           
                            
        pastMove1.append(input("Select New Postion"))
        print(pastMove1)

        newPOSX  = int(pastMove1[i][0:1]) #temp coordinates
        newPOSY  =  int(pastMove1[i][2:3])
        print(newPOSX,newPOSY)  

        if (grid[newPOSX][newPOSY] == "_ "):
           
            grid[newPOSX][newPOSY] = "B "  #changes the avilabe space to B and the last space to _
            grid[toRows][toCols] = "_ "
            checkForOpponents(newPOSX, newPOSY, toRows ,toCols)
            king1 = checkStatus(newPOSX, newPOSY)
            
        
        elif (grid[newPOSX][newPOSY] != "_ "):
             pastMove1.pop(i)
             pastMove1.append(input("Unvalid Move! Select A New Postion"))
             newPOSX  = int (pastMove1[i][0:1]) #temp coordinates
             newPOSY  = int (pastMove1[i][2:3])

       
             

    return pastMove1, grid, toRows,toCols, i 

def checkForOpponents(newPOSX, newPOSY, toRows ,toCols): # only works when postions are valid.

    if ((newPOSY-toCols) == 2): 
        #Sqaure moves right 
        a = newPOSX - 1 #a and b coorindinates for opponent
        b = newPOSY - 1 
        if(grid[a][b] == "W " or (grid[a][b] == "w ")):
            grid[a][b] = "_ "
            
        elif(grid[a][b] == "_ " or grid[a][b] == "B "):
            print("No Piece to Take")
            
    if (newPOSY-toCols == -2): #sqaure moved left
      
        a = newPOSX -1
        b = newPOSY + 1
        
        if(grid[a][b] == "W " or (grid[a][b] == "w ")):
            grid[a][b] = "_ "
            
                    
        elif(grid[a][b] == "_ " or grid[a][b] == "B "):
            print("No Piece to Take")
        

    return

def checkStatus(newPOSX, newPOSY):

    if(newPOSX == 7):
        grid[newPOSX][newPOSY] = "b "
        king1 = "b "
        return king1
    else:
        print("No king")
        return False
    

def kingMoves(toRows, toCols,i, pastMove1,curentMove1):
    print("I am king")

    avaPOSX = toRows + 1
    avaPOSY = toRows - 1
    avaPOSL = toCols - 1
    avaPOSR = toCols + 1

    
    #Valid pos
    POSX = toRows + 2
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

    newPOSX  = int (pastMove1[i][0:1]) #temp coordinates
    newPOSY  =  int (pastMove1[i][2:3])
    print(newPOSX,newPOSY)  

    if (grid[newPOSX][newPOSY] == "_ "):  
        grid[newPOSX][newPOSY] = "b "
        grid[toRows][toCols] = "_ "
        kingOpponents(newPOSX, newPOSY, toRows ,toCols)
                
    elif (grid[newPOSX][newPOSY] != "_ "):
        pastMove1.append(("Unvalid Move! Select A New Postion"))
        newPOSX  = int (pastMove1[0:1]) #temp coordinates
        newPOSY  = int (pastMove1[2:3])
            
        
    
    return grid

def kingOpponents(newPOSX, newPOSY, toRows ,toCols):
    if ((newPOSY - toCols) == 2):  #Sqaure moves right 
        if((newPOSX - toRows) == 2): #sqaure moved down
           
            a = newPOSX - 1 #a and b coorindinates for opponent
            b = newPOSY - 1
            print() 
            if(grid[a][b] == "W " or grid[a][b] == "w "):
                grid[a][b] = "_ "
            elif(grid[a][b] == "_ " or grid[a][b] == "B "):
                print("No Piece to Take")
                
        elif((newPOSX-toRows)== -2): #sqaure moved up
            a = newPOSX + 1 #a and b coorindinates for opponent
            b = newPOSY - 1
            print() 
            if(grid[a][b] == "W " or grid[a][b] == "w "):
                grid[a][b] = "_ "
            elif(grid[a][b] == "_ " or grid[a][b] == "B "):
                print("No Piece to Take")
        
        
            
    if (newPOSY-toCols == -2): #sqaure moved left
         if((newPOSX - toRows) == 2): #sqaure moved down
           
            a = newPOSX - 1 #a and b coorindinates for opponent
            b = newPOSY + 1
            if(grid[a][b] == "W " or grid[a][b] == "w "):
                grid[a][b] = "_ "
                
            elif(grid[a][b] == "_ " or grid[a][b] == "B "):
                print("No Piece to Take")
         elif((newPOSX-toRows)== -2): #sqaure moved up
            a = newPOSX + 1 #a and b coorindinates for opponent
            b = newPOSY + 1
            
            if(grid[a][b] == "W " or grid[a][b] == "w "):
                grid[a][b] = "_ "
            elif(grid[a][b] == "_ " or grid[a][b] == "B "):
                print("No Piece to Take")
      
    return newPOSX, newPOSY, toRows ,toCols
     
    
    


def secondMoves(j):
    print("Player 2's Turn")
    draw_grid(grid)
            
    currentMove2.append(input("Select piece to move"))
    if (currentMove2[j] == "undo"):
        currentMove2.pop()
        undo_feature(i,pastMove1,currentMove1)
    else:
        validPOS2(currentMove2, pastMove2,j)


    return grid

def validPOS2(currentMove2, pastMove2,j):
    toRows  = int (currentMove2[j][0:1]) #Converts the sliced string to an int
    toCols  = int (currentMove2[j][2:3])

    avaPOSX = toRows - 1 #chnages the coordinates to llok for the avaliable spaces near by
    avaPOSL = toCols - 1
    avaPOSR = toCols + 1

    POSX = toRows -2 #Looks for an open space either to the left or the right
    POSL = toCols -2
    POSR = toCols +2

    if(grid[toRows][toCols] == "w "):
    
        king2Moves(toRows, toCols,j, pastMove2,currentMove2)
    else:

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
                while(((grid[avaPOSX][avaPOSL] != "_ ") or (grid[avaPOSX][avaPOSR] != "_ ") or (grid[POSX][POSR] != "_ ") or( grid[POSX][POSL] != "_ "))  and response == False):

                    if (grid[avaPOSX][avaPOSL] == "_ " ):
                        response = True
                        
                    if (grid[POSX][POSL] == "_ " ):
                        if(grid[avaPOSX][avaPOSL] == "B " or grid[avaPOSX][avaPOSL] == "b "):
                            response = True
                
                    if (grid[avaPOSX][avaPOSR] == "_ "):
                        response = True 

                    if(grid[POSX][POSR] == "_ "):
                        if(grid[avaPOSX][avaPOSR] == "B " or grid[avaPOSX][avaPOSR] == "b "):
                            response = True
                        
                    
                    if((grid[avaPOSX][avaPOSL] != "_ ") and (grid[avaPOSX][avaPOSR] != "_ ") and (grid[POSX][POSR] != "_ ") and (grid[POSX][POSL] != "_ ")):
                            currentMove2.append(input("Select piece to move"))
                            toRows  = int (currentMove2[j][0:1]) #Converts the sliced string to an int
                            toCols  = int (currentMove2[j][2:3])

                            avaPOSX = toRows + 1 #chnages the coordinates to llok for the avaliable spaces near by
                            avaPOSL = toCols - 1
                            avaPOSR = toCols + 1
                
        pastMove2.append(input("Select New Postion"))
        newPOSX  = int (pastMove2[j][0:1]) #temp coordinates
        newPOSY  = int (pastMove2[j][2:3])

        print(pastMove2)
               
        if (grid[newPOSX][newPOSY] == "_ "):  
            grid[newPOSX][newPOSY] = "W "  #changes the avilabe space to B and the last space to _
            grid[toRows][toCols] = "_ "
            checkForOppo(newPOSX, newPOSY, toRows,toCols)
            king2 = check2Status(newPOSX, newPOSY)
            
        
        elif (grid[newPOSX][newPOSY] != "_ "):
             pastMove2 = input("Unvalid Move! Select A New Postion")
             newPOSX  = int (pastMove2[0:1]) #temp coordinates
             newPOSY  = int (pastMove2[2:3])

    return pastMove2, grid, toRows,toCols

def checkForOppo(newPOSX, newPOSY, toRows ,toCols): # only works when postions are valid.
    if ((newPOSY-toCols) == 2):
        #Sqaure moved right 
        a = newPOSX + 1 #a and b coorindinates for opponent
        b = newPOSY - 1
        
        if(grid[a][b] == "B " or grid[a][b] == "b "):
            grid[a][b] = "_ "
        elif(grid[a][b] == "_ " or grid[a][b] == "W "):
            print("No Piece to Take")
            
    if (newPOSY-toCols == -2): #sqaure moved left
        a = newPOSX + 1
        b = newPOSY + 1
        if(grid[a][b] == "B " or grid[a][b] == "b "):
            grid[a][b] = "_ "
        elif(grid[a][b] == "_ " or grid[a][b] == "W "):
            print("No Piece to Take")
        

    return 

def check2Status(newPOSX, newPOSY):

    if(newPOSX == 0):
        grid[newPOSX][newPOSY] = "w "
        king2 = "w "
        return king2
    else:
        print("No king")
        return False

def king2Moves(toRows, toCols, j, pastMove2):
    print("I am king")

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
            elif(grid[a][b] == "_ " or grid[a][b] == "W "):
                print("No Piece to Take")
                
        elif((newPOSX-toRows)== -2): #sqaure moved up
            a = newPOSX + 1 #a and b coorindinates for opponent
            b = newPOSY - 1
           
            if(grid[a][b] == "B " or grid[a][b] == "b "):
                grid[a][b] = "_ "
            elif(grid[a][b] == "_ " or grid[a][b] == "W "):
                print("No Piece to Take")
        
        
            
    if (newPOSY-toCols == -2): #sqaure moved left
         if((newPOSX - toRows) == 2): #sqaure moved down
           
            a = newPOSX - 1 #a and b coorindinates for opponent
            b = newPOSY + 1
            if(grid[a][b] == "B " or grid[a][b] == "b "):
                grid[a][b] = "_ "
            elif(grid[a][b] == "_ " or grid[a][b] == "W "):
                print("No Piece to Take")
                
         elif((newPOSX-toRows)== -2): #sqaure moved up
            a = newPOSX + 1 #a and b coorindinates for opponent
            b = newPOSY + 1
            
            if(grid[a][b] == "B " or grid[a][b] == "b "):
                grid[a][b] = "_ "
            elif(grid[a][b] == "_ " or grid[a][b] == "W "):
                print("No Piece to Take")

def AIMoves(j):
   
    for r in range(height):
        for c in range(width):
            if(grid[r][c] == "W "):
                 print(r,c)
                 checkIfMove(r,c,possibleStartMove,possibleEndMove)                
    print(possibleStartMove)
    print(possibleEndMove)
    selectPiece = random.choice(possibleStartMove)
    newPositionIndex = possibleStartMove.index(selectPiece)
    newPosition  = possibleEndMove[newPositionIndex]
    
    toRows  = selectPiece[0]#Converts the sliced string to an int
    toCols  = selectPiece[1]
    newRows = newPosition[0]
    newCols = newPosition[1]
    print(toRows, toCols)
    print(newRows, newCols)
    checkAIOpponents(newCols,toCols,newRows)

    grid[toRows][toCols] = "_ "
    grid[newRows][newCols] = "W "
    possibleStartMove.clear()
    possibleEndMove.clear()

def checkIfMove(r,c,possibleStartMove,possibleEndMove):
    avaPOSX = r - 1
    avaPOSL = c - 1
    avaPOSR = c + 1

    POSX = avaPOSX -1 #Looks for an open space either to the left or the right
    POSL = avaPOSL -1
    POSR = avaPOSR +1
    
    if((avaPOSX < 0 or avaPOSX > 7) or (avaPOSL <0 or avaPOSL > 7) or (avaPOSR < 0 or avaPOSR > 7)):
        return r, c
    else:
        print("entered the other section")
    
        if((grid[avaPOSX][avaPOSL] != "_ ") or (grid[avaPOSX][avaPOSR] != "_ ") or (grid[avaPOSX][avaPOSL] == "W ") or (grid[avaPOSX][avaPOSR] == "W ")):
            print(r,c, " Returned. No Value")

        if (grid[avaPOSX][avaPOSL] == "_ "):
            if((avaPOSX < 0 or avaPOSX > 7) or (avaPOSL < 0 or avaPOSL > 7)):
                if(grid[avaPOSX][avaPOSR]== "_ "):
                    print("Moved to the right")
                    possibleStartMove.append((r,c))
                    possibleEndMove.append((avaPOSX,avaPOSR))
                    return possibleStartMove, possibleEndMove
                else:
                    print("Excuse me ")
                    possibleStartMove.append((r,c))
                    possibleEndMove.append((avaPOSX,avaPOSL))
                    return possibleStartMove, possibleEndMove


        if(grid[avaPOSX][avaPOSR]== "_ "):
            if((avaPOSX < 0 or avaPOSX > 7) or (avaPOSR < 0 or avaPOSR > 7)):
                if (grid[avaPOSX][avaPOSL] == "_ "):
                    print("Moved to the left")
                    possibleStartMove.append((r,c))
                    possibleEndMove.append((avaPOSX,avaPOSL))
                    return possibleStartMove, possibleEndMove
            else:
                possibleStartMove.append((r,c))
                possibleEndMove.append((avaPOSX, avaPOSR))
                return possibleStartMove, possibleEndMove
##
##        if(grid[POSX][POSR] == "_ "):
##             if(grid[avaPOSX][avaPOSR] == "B "):
##                 possibleStartMove.append((r,c))
##                 possibleEndMove.append((POSX, POSR))
##                 return possibleStartMove, possibleEndMove
##                    
##        if(grid[POSX][POSL] == "_ "):
##             if(grid[avaPOSX][avaPOSL] == "B "):
##                 possibleStartMove.append((r,c))
##                 possibleEndMove.append((POSX, POSl))
##                 return possibleStartMove, possibleEndMove
                        

def checkAIOpponents(newCols,toCols,newRows):
    print("ENtered AI Oppo")
    if ((newCols-toCols) == 2):
        #Sqaure moved right 
        a = newRows + 1 #a and b coorindinates for opponent
        b = newCols - 1
        
        if(grid[a][b] == +" " or grid[a][b] == +" "):
            grid[a][b] = "_ "
            return  firstMove(i)
        elif(grid[a][b] == "_ " or grid[a][b] == +" "):
            print("No Piece to Take")
            
    if (newCols-toCols == -2): #sqaure moved left
        a = newRows + 1
        b = newCols + 1
        if(grid[a][b] == "B " or grid[a][b] == "b "):
            grid[a][b] = "_ "
            return  firstMove(i)
        elif(grid[a][b] == "_ " or grid[a][b] == +"W "):
            print("No Piece to Take")

    return
    
def undo_feature(i,pastMove1,currentMove1):
    i-=1
    print("Undo Selected")
    print(i)
    print(currentMove1[i])
    toRows  = int (currentMove1[i][0:1]) #Converts the sliced string to an int
    toCols  = int (currentMove1[i][2:3])
  
    newPOSX  = int (pastMove1[i][0:1]) #temp coordinates
    newPOSY  = int (pastMove1[i][2:3])
    print(pastMove1)
    
    currentMove1.pop()
    pastMove1.pop()

    if (grid[toRows][toCols] == "_ "):
           
            grid[newPOSX][newPOSY] = "_ "  #changes the avilabe space to B and the last space to _
            grid[toRows][toCols] = "B "
           
            print(i)
            print("Move Deleted")
            return firstMove(), i

def undo_feature_2(j,pastMove2,currentMove2):
    j-=1
    print("Undo Selected")
    print(j)
    print(currentMove2[j])
    toRows  = int (currentMove2[j][0:1]) #Converts the sliced string to an int
    toCols  = int (currentMove2[j][2:3])
  
    newPOSX  = int (pastMove2[j][0:1]) #temp coordinates
    newPOSY  = int (pastMove2[j][2:3])
    print(pastMove2)
    
    currentMove2.pop()
    pastMove2.pop()

    if (grid[toRows][toCols] == "_ "):
           
            grid[newPOSX][newPOSY] = "_ "  #changes the avilabe space to B and the last space to _
            grid[toRows][toCols] = "W "
           
            print(j)
            print("Move Deleted")
            return secondMoves(j)



#Issues found while playing:
    #Move other persons piece!
    #When error message occurs, no change to piece
    #Empty variables
    #Appending into liat when value has not been checked
    
          
##Global Variables
width = 8
height = 8
pastMove1=[]
pastMove2=[]
currentMove1=[]
currentMove2=[]
possibleStartMove =[]
possibleEndMove =[]


i = 0
j = 0                      

                       
#Main Program
instruction()
opponent = input("Select your opponent \n1. Computer\n2. Human")
if(opponent == '1'):
    print("You have selected Computer")
    grid = init_board()
    while(stilPieces(bool) == False):
        firstMove(i)
        i+=1
        AIMoves(j)
        j+=1
        
    print("Game Ended")
    
elif(opponent == '2'):
    print("You have selected human")
    grid = init_board()
    while(stilPieces(bool) == False):
        firstMove(i)
        i+=1
        secondMoves(j)
        j+=1
        
    print("Game Ended")
