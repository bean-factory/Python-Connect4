Players = ["Yellow","Red"]
L = []

InProgress = True
EndGame = False

#True for Red, False for Yellow
Player = True

R = "🔴"
Y = "🟡"

while EndGame == False:
    def init():
        #Setup board
        print("Rules:","1. Tokens will pile up from the bottom as you place them from the top.", "2. Only 1 move is allowed per turn, and only 2 players can play. Red Player moves first, followed by the Yellow Player", "3. First to connect 4 tokens horizontally or vertically wins.", "4. When it is your turn, specify the column number from the left. A white dot indicates a vacant space.","5. The current board will appear after each move.", sep = "\n") 
        while True:
            Width = input("Enter width: ")
            try:
                Width = int(Width)
            except ValueError:
                print("Must be between 4 and 20")
                continue 
            if 4 <= Width <= 20:
                break
            else:
                print("Must be between 4 and 20")
        
        while True:
            Height = int(input("Enter height: "))
            try:
                Height = int(Height)
            except ValueError:
                print("Must be between 4 and 20")
                continue 
            if 4 <= Height <= 20:
                break
            else:
                print("Must be between 4 and 20")
        
        for i in range(Height):
            L2 = []
            for j in range(Width):
                L2.append("⚪")
            L.append(L2)
    
    def draw():
        #Print board
        for i in L:
            for j in i:
                print(j,end="")
            print()
    
    def check():
        global L,InProgress
        
        #Horizontal Check
        for i in L:
            for j in range(0,len(i)-3):
                if i[j] == R and i[j+1] == R and i[j+2] == R and i[j+3] == R:
                    win()
                elif i[j] == Y and i[j+1] == Y and i[j+2] == Y and i[j+3] == Y:
                    win()
    
        #Vertical Check
        for i in range(len(L)-3):
            for j in range(0,len(L[i])):
                if L[i][j] == R and L[i+1][j] == R and L[i+2][j] == R and L[i+3][j] == R:
                    win()
                elif L[i][j] == Y and L[i+1][j] == Y and L[i+2][j] == Y and L[i+3][j] == Y:
                    win()
        
        #Draw Check
        if sum(i.count("⚪") for i in L) == 0:
            print("-"*25,"Draw!","-"*25)
            draw()
            InProgress = False
    
    def win():
        #Display Outcome
        global InProgress
        print("-"*25,Players[int(Player)],"Player has won!","-"*25)
        draw()
        InProgress = False
    
    def move():
        #Get Player move
        global Player, Players
            
        print("-"*25,Players[int(Player)],"Player's Turn","-"*25)
        C = R if Player == True else Y
        draw()
        
        while True:
            
            N = input("Enter column: ")
            
            try:
                N = int(N)
            except ValueError:
                print("-"*25,Players[int(Player)],"Player's Turn","-"*25)
                print("Illegal move, please try again.")
                draw()
                continue
    
            if 1 <= N <= len(L[0]) and L[0][N-1] == "⚪":
                break
            else:
                print("-"*25,Players[int(Player)],"Player's Turn","-"*25)
                print("Illegal move, please try again.")
                draw()
        
        for i in range(len(L)-1,-1,-1):
            if L[i][N-1] == "⚪":
                L[i][N-1] = C
                check()
                Player = not Player
                break
    
    #Start game
    init()
    while InProgress == True:
        move()
    while True:
        N = input("New game? (Y/N): ").upper()
        if N == "Y":
            L = []
            InProgress = True
            Player = True
            break
        if N == "N":
            EndGame = True
            break
