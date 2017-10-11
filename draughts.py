#class pieces

width = 8
height = 8

def draw_board():
    grid = [[0 for x in range(width)] for y in range(height)]

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
    print("0 1 2 3 4 5 6 7")
    for x in range(width):
        print("")
        for y in range(height):
            
            print(grid[x][y], end="")
    
            
    return grid
def firstPlayer():
   
    
    Player1 = input("Select who goes first. B/W")
    if(Player1 == "B"):
        Player2 = "W"
    else:
        Player2 = "B"
    print("Player 1", Player1)
    print("PLayer 2", Player2)

    return Player1, Player2

def firstMove(grid,Player1):
    pastMoves=[]
    for x in range(8):
        print("")
        for y in range(8):
            print(grid[x][y], end="")
    currentMove = input("Make first Move")
    if (pastMove != Player1):
        print("Not your piece")
        currentMoves = input("Player 1's Turn")
    else:
        pastMoves = input("Select New Postion")
        grid(currentMoves) == pastMoves
        
        

  
    
    


        
grid = draw_board()
firstPlayer()
firstMove(grid, Player1)

    
    


#Issues:


#def stealPiece()

#def doubleJump()

#def secondPlayer()

#def stillPieces()

#def endGame() 
