Players = ["Yellow Player's turn","Red Player's turn"]
Player = True
CRED = '\033[91m'
CEND = '\033[0m'
CYELLOW = '\33[33m'

while True:

    def init():
        global X,Y,L
        while True:
            X = int(input("Enter width: "))
            if X >= 4:
                break
            else:
                print("Must be atleast 4")
        while True:
            Y = int(input("Enter height: "))
            if Y >= 4:
                break
            else:
                print("Must be atleast 4")
        L = []
        for i in range(Y):
            L2 = []
            for j in range(X):
                L2.append("•")
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
                if i[j] == CRED+"•"+CEND and i[j+1] == CRED+"•"+CEND and i[j+2] == CRED+"•"+CEND and i[j+3] == CRED+"•"+CEND:
                    draw()
                    print("Red has won! ")
                    quit()
                elif i[j] == CYELLOW+"•"+CEND and i[j+1] == CYELLOW+"•"+CEND and i[j+2] == CYELLOW+"•"+CEND and i[j+3] == CYELLOW+"•"+CEND:
                    draw()
                    print("Yellow has won! ")
                    quit()
        for i in range(len(L)-3):
            for j in range(0,len(L[i])):
                if L[i][j] == CRED+"•"+CEND and L[i+1][j] == CRED+"•"+CEND and L[i+2][j] == CRED+"•"+CEND and L[i+3][j] == CRED+"•"+CEND:
                    draw()
                    print("Red has won! ")
                    quit()
                elif L[i][j] == CYELLOW+"•"+CEND and L[i+1][j] == CYELLOW+"•"+CEND and L[i+2][j] == CYELLOW+"•"+CEND and L[i+3][j] == CYELLOW+"•"+CEND:
                    draw()
                    print("Yellow has won! ")
                    quit()

    def move():
        global Player, Players
        while True:
            print("-"*25,Players[int(Player)],"-"*25)
            C = CRED+"•"+CEND if Player == True else CYELLOW+"•"+CEND
            draw()
            N = int(input("Enter column: "))
            if N <= X:
                for i in range(len(L)-1,-1,-1):
                    if L[i][N-1] == "•":
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
