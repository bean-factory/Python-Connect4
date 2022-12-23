InProgress = True
Players = ["Red Player's turn", "Yellow Player's turn"]
Player = True

while InProgress == True:

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
        pass

    def move():
        global Player, Players
        while True:
            print("-"*25,Players[int(Player)],"-"*25)
            C = "R" if Player == True else "Y"
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
