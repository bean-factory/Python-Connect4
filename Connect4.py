Players = ["Yellow","Red"]
L = []

InProgress = True
EndGame = False

#True for Red, False for Yellow
Player = True

R = "🔴"
Y = "🟡"
E = "⚪"

def init():
    #Setup board
    print("Rules:","1. Tokens will pile up from the bottom as you place them from the top.", "2. Only 1 move is allowed per turn, and only 2 players can play. Red Player moves first, followed by the Yellow Player", "3. First to connect 4 tokens horizontally, vertically or diagonally wins.", "4. When it is your turn, specify the column number from the left. A white dot indicates a vacant space.","5. The current board will appear after each move.", sep = "\n") 
   
    while True:
        Width = input("Enter width: ")
        try:
            Width = int(Width)
            if Width < 4 or Width > 20:
                raise ValueError
        except ValueError:
            print("Must be between 4 and 20")
            continue
        break
    
    while True:
        Height = int(input("Enter height: "))
        try:
            Height = int(Height)
            if Height < 4 or Height > 20:
                raise ValueError
        except ValueError:
            print("Must be between 4 and 20")
            continue
        break
    
    for i in range(Height):
        L2 = []
        for j in range(Width):
            L2.append(E)
        L.append(L2)

def board():
    #Print board
    for i in L:
        for j in i:
            print(j,end="")
        print()

def check():
    #Horizontal Check
    for i in L:
        for j in range(0,len(i)-3):
            if i[j:j+4] == [R, R, R, R] or i[j:j+4] == [Y, Y, Y, Y]:
                win()
                return True
    
    #Vertical Check
    for i in range(len(L)-3):
        for j in range(0,len(L[i])):
            if L[i][j] == L[i+1][j] == L[i+2][j] == L[i+3][j] and L[i][j] != E:
                win()
                return True
    
    #Diagonal Check (top left to bottom right)
    for i in range(len(L)-3):
        for j in range(0,len(L[i])-3):
            if L[i][j] == L[i+1][j+1] == L[i+2][j+2] == L[i+3][j+3] and L[i][j] != E:
                win()
                return True
    
    #Diagonal Check (top right to bottom left)
    for i in range(len(L)-3):
        for j in range(0,len(L[i])-3):
            if L[i][::-1][j] == L[i+1][::-1][j+1] == L[i+2][::-1][j+2] == L[i+3][::-1][j+3] and L[i][::-1][j] != E:
                win()
                return True
    #Draw Check
    if sum(i.count(E) for i in L) == 0:
        win("Draw")
        return True

def win(outcome="Not Draw"):
    #Display Outcome
    if outcome == "Draw":
        print("-"*25,outcome,"-"*25)
    else:
        print("-"*25,Players[int(not Player)],"Player has won!","-"*25)
    board()

def move():
    #Get Player move
    global Player, Players
        
    print("-"*25,Players[int(Player)],"Player's Turn","-"*25)
    C = R if Player == True else Y
    board()
    
    while True:
        N = input("Enter column: ")    
        try:
            N = int(N)
            if N < 1 or N > len(L[0]) or L[0][N-1] != E:
                raise ValueError
        except ValueError:
            print("-"*25,Players[int(Player)],"Player's Turn","-"*25)
            print("Illegal move, please try again.")
            board()
            continue
        break
    
    for i in range(len(L)-1,-1,-1):
        if L[i][N-1] == E:
            L[i][N-1] = C
            Player = not Player
            break

while EndGame == False: 
    #Start game
    init()
    
    while not check():
        move()

    while True:
        N = input("New game? (Y/N): ").upper()
        if N == "Y":
            L = []
            Player = True
            break
        if N == "N":
            EndGame = True
            break
        print("Invalid choice, try again.")
