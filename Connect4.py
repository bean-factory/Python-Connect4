Players = ["Yellow Player's turn","Red Player's turn"]
#True for Red, False for Yellow
Player = True
#ANSI codes for colored output
Red = '\033[91m'
End = '\033[0m'
Yellow = '\33[33m'
R = Red+"⬤"+End
Y = Yellow+"⬤"+End

while True:

    def init():
        #Setup board
        global Height,Height,L
        
        while True:
            Height = input("Enter width: ")
            try:
                Height = int(Height)
            except ValueError:
                print("Must be between 4 and 20")
                continue 
            if 4 <= Height <= 20:
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
        
        L = []
        
        for i in range(Height):
            L2 = []
            for j in range(Height):
                L2.append("⬤")
            L.append(L2)
    
    def draw():
        #Print board
        for i in L:
            for j in i:
                print(j,end="  ")
            print()
    
    def check():
        global L
        
        #Horizontal Check
        for i in L:
            for j in range(0,len(i)-3):
                if i[j] == R and i[j+1] == R and i[j+2] == R and i[j+3] == R:
                    draw()
                    print("Red has won!")
                    quit()
                elif i[j] == Y and i[j+1] == Y and i[j+2] == Y and i[j+3] == Y:
                    draw()
                    print("Yellow has won!")
                    quit()

        #Vertical Check
        for i in range(len(L)-3):
            for j in range(0,len(L[i])):
                if L[i][j] == R and L[i+1][j] == R and L[i+2][j] == R and L[i+3][j] == R:
                    draw()
                    print("Red has won! ")
                    quit()
                elif L[i][j] == Y and L[i+1][j] == Y and L[i+2][j] == Y and L[i+3][j] == Y:
                    draw()
                    print("Yellow has won! ")
                    quit()
        
        #Draw Check
        if sum(i.count("⬤") for i in L) == 0:
            draw()
            print("Draw!")
            quit()

    def move():
        #Get Player move
        global Player, Players

        while True:
            
            print("-"*25,Players[int(Player)],"-"*25)
            C = R if Player == True else Y
            draw()
            
            while True:
                
                N = input('Enter column: ')
                
                try:
                    N = int(N)
                except ValueError:
                    print("Illegal move, please try again.")
                    print("-"*25,Players[int(Player)],"-"*25)
                    draw()
                    continue
                if 1 <= N <= len(L[0]):
                    break
                else:
                    print("Illegal move, please try again.")
                    print("-"*25,Players[int(Player)],"-"*25)
                    draw()
            
            for i in range(len(L)-1,-1,-1):
                if L[i][N-1] == "⬤":
                    L[i][N-1] = C
                    Player = not Player
                    check()
                    break
            else:
                print("Illegal move, please try again.")

    init()
    move()
