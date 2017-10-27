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
    pastMove1=[]
            
    currentMove = input("Select piece to move")

    validPOS1(Player1, Player2, grid, currentMove, pastMove1) #Another Function
    checkStatus(Player1, Player2)

    return grid

def validPOS1(Player1, Player2, grid, currentMove, pastMove1):
    toRows  = int (currentMove[0:1]) #Converts the sliced string to an int
    toCols  = int (currentMove[2:3])

    avaPOSX = toRows + 1 #chnages the coordinates to llok for the avaliable spaces near by
    avaPOSL = toCols - 1
    avaPOSR = toCols + 1

    POSX = avaPOSX +1
    POSL = avaPOSL -1
    POSR = avaPOSR +1

    response = False

    
    if ((avaPOSX in range(0,7)) and ((avaPOSL in range (0,7)) or (avaPOSR in range(0,7)))):
        while ((grid[avaPOSX][avaPOSL] != "_ ") or (grid[avaPOSX][avaPOSR] != "_ ") and response == False):


            if (grid[avaPOSX][avaPOSL] == "_ "):
                        response = True
                    
            elif (grid[avaPOSX][avaPOSR] == "_ "):
            
                response = True
                    
            if((grid[POSX][POSL] == "_ ") and (grid[avaPOSX][avaPOSL] == Player2)):
                response = True
            
            
            if(grid[avaPOSX][avaPOSL] != "_ " and grid[avaPOSX][avaPOSR] != "_ "):
                    
                currentMove = input("Selcet A Moveable Piece")
                toRows  = int (currentMove[0:1]) #Converts the sliced string to an int
                toCols  = int (currentMove[2:3])

                avaPOSX = toRows + 1 #chnages the coordinates to llok for the avaliable spaces near by
                avaPOSL = toCols - 1
                avaPOSR = toCols + 1
                
           
                    
            
    pastMove1 = input("Select New Postion")

    newPOSX  = int (pastMove1[0:1]) #temp coordinates
    newPOSY  = int (pastMove1[2:3])

    re = False

    #while (grid[newPOSX][newPOSY] != "_ " and re == False):

    if (grid[newPOSX][newPOSY] == "_ "):  
      
        grid.append(pastMove1)
        grid[newPOSX][newPOSY] = Player1+" "  #changes the avilabe space to B and the last space to _
        grid[toRows][toCols] = "_ "
        checkForOpponents(grid, p2Pieces, newPOSX, newPOSY, toRows  ,toCols)
        
    
    elif (grid[newPOSX][newPOSY] != "_ "):
         pastMove1 = input("Unvalid Move! Select A New Postion")
         newPOSX  = int (pastMove1[0:1]) #temp coordinates
         newPOSY  = int (pastMove1[2:3])
         

    return pastMove1, grid

def checkForOpponents(grid, p2Pieces, newPOSX, newPOSY, toRows ,toCols): # only works when postions are valid.

    if ((newPOSY-toCols) == 2): 
        #Sqaure moves right 
        a = newPOSX - 1 #a and b coorindinates for opponent
        b = newPOSY - 1
        print(Player2) 
        if(grid[a][b] == Player2+" "):
            grid[a][b] = "_ "
            p2Pieces = p2Pieces - 1
        elif(grid[a][b] == "_ " or grid[a][b] == Player1+" "):
            print("No Piece to Take")
            
    if (newPOSY-toCols == -2): #sqaure moved left
      
        a = newPOSX -1
        b = newPOSY + 1
        
        if(grid[a][b] == Player2+" "):
            grid[a][b] = "_ "
            p2Pieces = p2Pieces - 1
            print(p1Pieces)
                    
        elif(grid[a][b] == "_ " or grid[a][b] == Player1+" "):
            print("No Piece to Take")

    #doubleJump1(newPOSX, newPOSY,Player2,p2Pieces)
        

    return p2Pieces, grid

def doubleJump1(newPOSX, newPOSY,Player2,p2Pieces):

    print("I have entereed the dj")
    newPo1X = newPOSX +1
    newPo1Y = newPOSY +1

    newPo2X = newPOSX + 2
    newPo2Y = newPOSY + 2

    if ((newPo2X > 7) and (newPo2Y > 7)):
        print("Out of Range")
        return grid
    else:
        if((grid[newPo2X][newPo2Y] == "_ ") and (grid[newPo1X][newPo1Y]== Player2+" ")):
            answer = input("Would you Like to make an addtional move? Y/N")
            if (answer == "Y"):
                grid[newPo2X][newPo2Y] = Player1+""
                grid[newPo1X][newPo1Y] = "_ "
                p2Pieces-=1

                return grid
            else:
                return grid

def checkStatus(Player1, Player2):
    if(Player1 == grid[7]):
        king1 = Player1.lower()
        print("TO THE KING!!")
    else:
        print("NO KING!")
        return False
    if (Player2 == grid[0]):
        
        king2 = Player2.lower()
        print("TO THE KING!!")
    else:
        print("NO KING!!")
        return False
    
    
    


def secondMoves(Player2):
    print("Player 2's Turn")
    pastMove2=[]

    draw_grid(grid)
            
    currentMove = input("Select piece to move")
    validPOS2(Player2, grid, currentMove, pastMove2)
    checkStatus(Player1, Player2)


    return grid

def validPOS2(Player2, grid, currentMove, pastMove2):
    toRows  = int (currentMove[0:1]) #Converts the sliced string to an int
    toCols  = int (currentMove[2:3])

    avaPOSX = toRows - 1 #chnages the coordinates to llok for the avaliable spaces near by
    avaPOSL = toCols - 1
    avaPOSR = toCols + 1

    POSX = toRows -2 #Looks for an open space either to the left or the right
    POSL = toCols -2
    POSR = toCols +2

    response = False

    if ((avaPOSX in range(0,7)) and ((avaPOSL in range (0,7)) or (avaPOSR in range(0,7)))):
        while(((grid[avaPOSX][avaPOSL] != "_ ") or (grid[avaPOSX][avaPOSR] != "_ ") or (grid[POSX][POSR] != "_ ") or( grid[POSX][POSL] != "_ "))  and response == False):

             if (grid[avaPOSX][avaPOSL] == "_ "):
                            response = True
                        
             elif (grid[avaPOSX][avaPOSR] == "_ "):
                
                    response = True
                        
             if((grid[POSX][POSL] == "_ ") and (grid[avaPOSX][avaPOSL] == Player1)):
                    response = True
                
                
            
             if((grid[avaPOSX][avaPOSL] != "_ ") and (grid[avaPOSX][avaPOSR] != "_ ")):
                    currentMove = input("Selcet A Moveable Piece")
                    toRows  = int (currentMove[0:1]) #Converts the sliced string to an int
                    toCols  = int (currentMove[2:3])

                    avaPOSX = toRows + 1 #chnages the coordinates to llok for the avaliable spaces near by
                    avaPOSL = toCols - 1
                    avaPOSR = toCols + 1
                        
            
    pastMove2 = input("Select New Postion")

    newPOSX  = int (pastMove2[0:1]) #temp coordinates
    newPOSY  = int (pastMove2[2:3])
    #re = False

    #while ((grid[newPOSX][newPOSY] != "_ ") and re == False):        
    if (grid[newPOSX][newPOSY] == "_ "):  
      
        grid.append(pastMove2)
        grid[newPOSX][newPOSY] = Player2+" "  #changes the avilabe space to B and the last space to _
        grid[toRows][toCols] = "_ "
        checkForOppo(grid, p1Pieces, newPOSX, newPOSY, toRows  ,toCols)
        
    
    elif (grid[newPOSX][newPOSY] != "_ "):
         pastMove2 = input("Unvalid Move! Select A New Postion")
         newPOSX  = int (pastMove2[0:1]) #temp coordinates
         newPOSY  = int (pastMove2[2:3])

    return pastMove2, grid, toRows,toCols

def checkForOppo(grid, p1Pieces, newPOSX, newPOSY, toRows ,toCols): # only works when postions are valid.
    if ((newPOSY-toCols) == 2):
        #Sqaure moved right 
        a = newPOSX + 1 #a and b coorindinates for opponent
        b = newPOSY - 1
        
        if(grid[a][b] == Player1+" "):
            grid[a][b] = "_ "
            p1Pieces = p1Pieces - 1
            print(p1Pieces)
        if(grid[a][b] == "_ " or grid[a][b] == Player2+" "):
            print("No Piece to Take")
            
    if (newPOSY-toCols == -2): #sqaure moved left
        a = newPOSX + 1
        b = newPOSY + 1
        print(a, b)

        if(grid[a][b] == Player1+" "):
            grid[a][b] = "_ "
            p1Pieces = p1Pieces - 1
            print(p1Pieces)
        

    return p2Pieces, grid
          
##Global Variables
width = 8
height = 8
p1Pieces = 12
p2Pieces = 12

#Main Program
grid = init_board()
(Player1, Player2) = setPlayers()

while((p1Pieces != 0) or (p2Pieces !=0)):
    firstMove(Player1)
    secondMoves(Player2)
  
