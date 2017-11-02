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

def stilPieces():
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


def setPlayers(): 
   Player1 = input("Select Player 1's Piece. B/W")
   response = False
   
   while((Player1 != "B" or Player1 != "W") and response == False):
       if(Player1 == "B"):
           response = True
           Player2 = "W"
           return Player1, Player2
           
       elif (Player1 == "W"):
            Player2 = "B"
            response = True
            return Player1, Player2
        
       if(Player1 != "B" or Player1 != "W"):
           Player1 = input("Select Player 1's Piece. B/W")
        

def firstMove(Player1):
    print("Player 1's Turn")
    draw_grid(grid)
    response = False
            
    currentMove = input("Select piece to move")
    validPOS1(Player1, Player2, currentMove,pastMove1,i) #Another Function
    stilPieces()

    return grid

def validPOS1(Player1, Player2, currentMove,pastMove1,i):
    toRows  = int (currentMove[0:1]) #Converts the sliced string to an int
    toCols  = int (currentMove[2:3])

    avaPOSX = toRows + 1 #chnages the coordinates to llok for the avaliable spaces near by
    avaPOSL = toCols - 1
    avaPOSR = toCols + 1

    POSX = toRows + 2
    POSL = toCols - 2
    POSR = toCols + 2


    if(grid[toRows][toCols] == Player1.lower()+" "):
    
        kingMoves(toRows, toCols,i, pastMove1)
    else:
        
        response = False
        
        if((toRows < 0 or toRows >7) or (toCols < 0 or toCols > 7)): #checks if the input is in range
            if((avaPOSX <0 or avaPOSX > 7) or (avaPOSL <0 or avaPOSL >7) or (avaPOSR <0 and avaPOSR >7)):#checka whether the avalaible pos are in range
                print("Out of Range")
                currentMove = input("Select piece to move") 

                avaPOSX = toRows + 1
                avaPOSL = toCols - 1
                avaPOSR = toCols + 1
                
                
            else:
                while(((grid[avaPOSX][avaPOSL] != "_ ") or (grid[avaPOSX][avaPOSR] != "_ ") or (grid[POSX][POSR] != "_ ")
                       or( grid[POSX][POSL] != "_ "))  and response == False):

                    if (grid[avaPOSX][avaPOSL] == "_ " ): #if the ava POS has a space
                        response = True

                    if (grid[POSX][POSL] == "_ " ): # check if there was a free spot 2 spaces away and then checks if pplayer 2 is a spot away. 
                        if(grid[avaPOSX][avaPOSL] == Player2+" " or grid[avaPOSX][avaPOSR] == Player2.lower()+" "): 
                            response = True
                
                    elif (grid[avaPOSX][avaPOSR] == "_ "): 
                        response = True
               
                
                    elif(grid[POSX][POSR] == "_ "):
                        if(grid[avaPOSX][avaPOSR] == Player2+" " or grid[avaPOSX][avaPOSR] == Player2,lower()+" " ):
                            response = True
                        
                    
                    if((grid[avaPOSX][avaPOSL] != "_ ") and (grid[avaPOSX][avaPOSR] != "_ ") and (grid[POSX][POSR] != "_ ") and (grid[POSX][POSL] != "_ ")):
                            currentMove = input("Selcet A Moveable Piece")
                            toRows  = int (currentMove[0:1]) #Converts the sliced string to an int
                            toCols  = int (currentMove[2:3])

                            avaPOSX = toRows + 1 #chnages the coordinates to llok for the avaliable spaces near by
                            avaPOSL = toCols - 1
                            avaPOSR = toCols + 1
           
                            
        pastMove1.append(input("Select New Postion"))
        print(pastMove1)

        newPOSX  = int(pastMove1[i][0:1]) #temp coordinates
        newPOSY  =  int(pastMove1[i][2:3])
        print(newPOSX,newPOSY)  

        if (grid[newPOSX][newPOSY] == "_ "):
           
            grid[newPOSX][newPOSY] = Player1+" "  #changes the avilabe space to B and the last space to _
            grid[toRows][toCols] = "_ "
            checkForOpponents(newPOSX, newPOSY, toRows ,toCols)
            king1 = checkStatus(Player1, newPOSX, newPOSY)
            
        
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
        if(grid[a][b] == Player2+" " or (grid[a][b] == Player2.lower()+" ")):
            grid[a][b] = "_ "
            
        elif(grid[a][b] == "_ " or grid[a][b] == Player1+" "):
            print("No Piece to Take")
            
    if (newPOSY-toCols == -2): #sqaure moved left
      
        a = newPOSX -1
        b = newPOSY + 1
        
        if(grid[a][b] == Player2+" " or (grid[a][b] == Player2.lower()+" ")):
            grid[a][b] = "_ "
            
                    
        elif(grid[a][b] == "_ " or grid[a][b] == Player1+" "):
            print("No Piece to Take")
        

    return

def checkStatus(Player1,newPOSX, newPOSY):

    if(newPOSX == 7):
        grid[newPOSX][newPOSY] = Player1.lower()+" "
        king1 = Player1.lower()+" "
        return king1
    else:
        print("No king")
        return False
    

def kingMoves(toRows, toCols,i, pastMove1):
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
            currentMove = input("Select piece to move")

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
                    if(grid[avaPOSX][avaPOSL] == Player2+" " or grid[avaPOSX][avaPOSL] == Player2.lower()+" "):
                        response = True
                if(grid[POSY][POSL] == "_ "):
                    response = True
            
                elif (grid[avaPOSX][avaPOSR] == "_ "):
                    response = True
                    
                elif(grid[avaPOSY][avaPOSR] == "_ "):
                     response = True
            
                elif(grid[POSX][POSR] == "_ "):
                    if(grid[avaPOSX][avaPOSR] == Player2+" " or grid[avaPOSX][avaPOSR] == Player2.lower()+" "):
                        response = True
                    
                elif(grid[POSY][POSR] == "_ "):
                    if(grid[avaPOSY][avaPOSR] == Player2+" " or grid[avaPOSY][avaPOSR] == Player2.lower()+" "):
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
        grid[newPOSX][newPOSY] = Player1.lower()+" "
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
            print(Player2) 
            if(grid[a][b] == Player2+" " or grid[a][b] == Player2.lower()+" "):
                grid[a][b] = "_ "
            elif(grid[a][b] == "_ " or grid[a][b] == Player1+" "):
                print("No Piece to Take")
                
        elif((newPOSX-toRows)== -2): #sqaure moved up
            a = newPOSX + 1 #a and b coorindinates for opponent
            b = newPOSY - 1
            print(Player2) 
            if(grid[a][b] == Player2+" " or grid[a][b] == Player2.lower()+" "):
                grid[a][b] = "_ "
            elif(grid[a][b] == "_ " or grid[a][b] == Player1+" "):
                print("No Piece to Take")
        
        
            
    if (newPOSY-toCols == -2): #sqaure moved left
         if((newPOSX - toRows) == 2): #sqaure moved down
           
            a = newPOSX - 1 #a and b coorindinates for opponent
            b = newPOSY + 1
            if(grid[a][b] == Player2+" " or grid[a][b] == Player2.lower()+" "):
                grid[a][b] = "_ "
                
            elif(grid[a][b] == "_ " or grid[a][b] == Player1+" "):
                print("No Piece to Take")
         elif((newPOSX-toRows)== -2): #sqaure moved up
            a = newPOSX + 1 #a and b coorindinates for opponent
            b = newPOSY + 1
            
            if(grid[a][b] == Player2+" " or grid[a][b] == Player2.lower()+" "):
                grid[a][b] = "_ "
            elif(grid[a][b] == "_ " or grid[a][b] == Player1+" "):
                print("No Piece to Take")
      
    return newPOSX, newPOSY, toRows ,toCols
     
    
    


def secondMoves(Player2):
    print("Player 2's Turn")
    draw_grid(grid)
            
    currentMove = input("Select piece to move")
    validPOS2(Player2, currentMove, pastMove2)


    return grid

def validPOS2(Player2, currentMove, pastMove2):
    toRows  = int (currentMove[0:1]) #Converts the sliced string to an int
    toCols  = int (currentMove[2:3])

    avaPOSX = toRows - 1 #chnages the coordinates to llok for the avaliable spaces near by
    avaPOSL = toCols - 1
    avaPOSR = toCols + 1

    POSX = toRows -2 #Looks for an open space either to the left or the right
    POSL = toCols -2
    POSR = toCols +2

    if(grid[toRows][toCols] == Player2.lower()+" "):
    
        king2Moves(toRows, toCols,j, pastMove2)
    else:

        response = False
        if((toRows < 0 or toRows >7) or (toCols < 0 or toCols > 7)):
            if((avaPOSX <0 or avaPOSX > 7) or (avaPOSL <0 or avaPOSL >7) or (avaPOSR <0 and avaPOSR >7)):
                while(((grid[avaPOSX][avaPOSL] != "_ ") or (grid[avaPOSX][avaPOSR] != "_ ") or (grid[POSX][POSR] != "_ ") or( grid[POSX][POSL] != "_ "))  and response == False):

                    if (grid[avaPOSX][avaPOSL] == "_ " ):
                        response = True
                        
                    if (grid[POSX][POSL] == "_ " ):
                        if(grid[avaPOSX][avaPOSL] == Player1+" " or grid[avaPOSX][avaPOSL] == Player1.lowert()+" "):
                            response = True
                
                    if (grid[avaPOSX][avaPOSR] == "_ "):
                        response = True 

                    if(grid[POSX][POSR] == "_ "):
                        if(grid[avaPOSX][avaPOSR] == Player1+" " or grid[avaPOSX][avaPOSR] == Player1.lower()+" "):
                            response = True
                        
                    
                    if((grid[avaPOSX][avaPOSL] != "_ ") and (grid[avaPOSX][avaPOSR] != "_ ") and (grid[POSX][POSR] != "_ ") and (grid[POSX][POSL] != "_ ")):
                            currentMove = input("Selcet A Moveable Piece")
                            toRows  = int (currentMove[0:1]) #Converts the sliced string to an int
                            toCols  = int (currentMove[2:3])

                            avaPOSX = toRows + 1 #chnages the coordinates to llok for the avaliable spaces near by
                            avaPOSL = toCols - 1
                            avaPOSR = toCols + 1
                    
        pastMove2.append(input("Select New Postion"))
        newPOSX  = int (pastMove2[j][0:1]) #temp coordinates
        newPOSY  = int (pastMove2[j][2:3])

        print(pastMove2)
               
        if (grid[newPOSX][newPOSY] == "_ "):  
            grid[newPOSX][newPOSY] = Player2+" "  #changes the avilabe space to B and the last space to _
            grid[toRows][toCols] = "_ "
            checkForOppo(newPOSX, newPOSY, toRows,toCols)
            king2 = check2Status(Player2, newPOSX, newPOSY)
            
        
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
        
        if(grid[a][b] == Player1+" " or grid[a][b] == Player1.lower()+" "):
            grid[a][b] = "_ "
        elif(grid[a][b] == "_ " or grid[a][b] == Player2+" "):
            print("No Piece to Take")
            
    if (newPOSY-toCols == -2): #sqaure moved left
        a = newPOSX + 1
        b = newPOSY + 1
        if(grid[a][b] == Player1+" " or grid[a][b] == Player1.lower()+" "):
            grid[a][b] = "_ "
        elif(grid[a][b] == "_ " or grid[a][b] == Player2+" "):
            print("No Piece to Take")
        

    return 

def check2Status(Player1,newPOSX, newPOSY):

    if(newPOSX == 0):
        grid[newPOSX][newPOSY] = Player2.lower()+" "
        king2 = Player2.lower()+" "
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
            currentMove = input("Select piece to move")

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
                    if(grid[avaPOSX][avaPOSL] == Player1+" " or grid[avaPOSX][avaPOSL] == Player1.lower()+" "):
                        response = True
                        
                if(grid[POSY][POSL] == "_ "):
                    if(grid[avaPOSY][avaPOSL] == Player1+" " or grid[avaPOSY][avaPOSL] == Player1.lower()+" "):
                        response = True
            
                elif (grid[avaPOSX][avaPOSR] == "_ "):
                    response = True
                    
                elif(grid[avaPOSY][avaPOSR] == "_ "):
                     response = True
            
                elif(grid[POSX][POSR] == "_ "):
                    if(grid[avaPOSX][avaPOSR] == Player1+" " or grid[avaPOSX][avaPOSR] == Player1.lower()+" "):
                        response = True
                    
                elif(grid[POSY][POSR] == "_ "):
                    if(grid[avaPOSY][avaPOSR] == Player1+" " or grid[avaPOSY][avaPOSR] == Player1.lower()+" "):
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
       
                        
            
    pastMove2.append(input("Select New Postion"))
    print(pastMove2)

    newPOSX  = int (pastMove2[j][0:1]) #temp coordinates
    newPOSY  = int (pastMove2[j][2:3])
        
    if (grid[newPOSX][newPOSY] == "_ "):  
      
        grid[newPOSX][newPOSY] = Player2.lower()+" "  #changes the avilabe space to B and the last space to _
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
            if(grid[a][b] == Player1+" " or grid[a][b] == Player1.lower()+" "):
                grid[a][b] = "_ "
            elif(grid[a][b] == "_ " or grid[a][b] == Player2+" "):
                print("No Piece to Take")
                
        elif((newPOSX-toRows)== -2): #sqaure moved up
            a = newPOSX + 1 #a and b coorindinates for opponent
            b = newPOSY - 1
           
            if(grid[a][b] == Player1+" " or grid[a][b] == Player1.lower()+" "):
                grid[a][b] = "_ "
            elif(grid[a][b] == "_ " or grid[a][b] == Player2+" "):
                print("No Piece to Take")
        
        
            
    if (newPOSY-toCols == -2): #sqaure moved left
         if((newPOSX - toRows) == 2): #sqaure moved down
           
            a = newPOSX - 1 #a and b coorindinates for opponent
            b = newPOSY + 1
            if(grid[a][b] == Player1+" " or grid[a][b] == Player1.lower()+" "):
                grid[a][b] = "_ "
            elif(grid[a][b] == "_ " or grid[a][b] == Player2+" "):
                print("No Piece to Take")
                
         elif((newPOSX-toRows)== -2): #sqaure moved up
            a = newPOSX + 1 #a and b coorindinates for opponent
            b = newPOSY + 1
            
            if(grid[a][b] == Player1+" " or grid[a][b] == Player1.lower()+" "):
                grid[a][b] = "_ "
            elif(grid[a][b] == "_ " or grid[a][b] == Player2+" "):
                print("No Piece to Take")

#Issues found while playing:
    #Move other persons piece!
    #When error message occurs, no change to piece
    #Empty variables
    #Appending into liat when value has not been checked
    
          
##Global Variables
width = 8
height = 8                     
i = 0
j = 0                      
pastMove1=[]
pastMove2=[]
                       
#Main Program
grid = init_board()
(Player1, Player2) = setPlayers()
while(stilPieces(bool) == False):
    firstMove(Player1)
    i+=1
    secondMoves(Player2)
    j+=1
    
print("Game Ended")
