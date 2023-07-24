import random
def gamewin():
    print("WELCOME TO SCISSORS PAPER ROCK GAME!!!")
    print("ENTER 1 FOR SCISSORS")
    print("ENTER 2 FOR PAPER")
    print("ENTER 3 FOR ROCK")
    PC = random.randint(1,3)
    Player = int(input("enter your choice:"))
    attempts = 0
    while PC != Player:
        while attempts<=10:
         
         
         attempts+=1


         if PC == 1 and Player == 3:
            print("you won!!")
         elif PC == 2 and Player == 1:
            print("you won")
         elif PC == 3 and Player == 2:
            print("you won")
         elif PC == 2 and Player == 3:
            print("you lost,try again.")
         elif PC== 1 and Player == 2:
            print("you lost,try again")
         else:
            print("you lost,try again")
            break
gamewin()

