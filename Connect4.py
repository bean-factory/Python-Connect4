Players = ["Yellow Player's turn","Red Player's turn"]
Player = True
CRED = '\033[91m'
CEND = '\033[0m'
CYELLOW = '\33[33m'
R = CRED+"⬤"+CEND
Y = CYELLOW+"⬤"+CEND

while True:

    def init():
        global Length,Width,L
        while True:
            Length = int(input("Enter width: "))
            if Length >= 4:
                break
            else:
                print("Must be atleast 4")
        while True:
            Width = int(input("Enter height: "))
            if Width >= 4:
                break
            else:
                print("Must be atleast 4")
        L = []
        for i in range(Width):
            L2 = []
            for j in range(Length):
                L2.append("⬤")
            L.append(L2)
    
    def draw():
        for i in L:
            for j in i:
                print(j,end="  ")
            print()
    
    def check():
        global L
        for i in L:
            for j in range(0,len(i)-3):
                if i[j] == R and i[j+1] == R and i[j+2] == R and i[j+3] == R:
                    draw()
                    print("Red has won! ")
                    quit()
                elif i[j] == Y and i[j+1] == Y and i[j+2] == Y and i[j+3] == Y:
                    draw()
                    print("Yellow has won! ")
                    quit()
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

    def move():
        global Player, Players
        while True:
            print("-"*25,Players[int(Player)],"-"*25)
            C = R if Player == True else Y
            draw()
            N = int(input("Enter column: "))
            if N <= Length:
                for i in range(len(L)-1,-1,-1):
                    if L[i][N-1] == "⬤":
                        L[i][N-1] = C
                        Player = not Player
                        check()
                        break
                else:
                    print("Illegal move, please try again.")
            else:
                print("Illegal move, please try again.")
                draw()

    init()
    move()
