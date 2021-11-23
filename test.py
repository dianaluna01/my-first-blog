from random import randint

n = ["Rock", "Paper", "Scissors"]

player_1 = n[randint(0,2)]
print(player_1)
player_2 = False   

while player_2 == False: #sets player_2 to false so that game can continue
#set player_2 to True
    player_2 = input("Rock, Paper, Scissors?") #player_2 = true since it now has a value
    if player_2 == player_1:
        print("Tie!")
    elif player_2 == "Rock":
        if player_1 == "Paper":
            print("You lose!", player_1, "covers", player_2)
        else:
            print("You win!", player_2, "smashes", player_1)
    elif player_2 == "Paper":
        if player_1 == "Scissors":
            print("You lose!", player_1, "cut", player_2)
        else:
            print("You win!", player_2, "covers", player_1)
    elif player_2 == "Scissors":
        if player_1 == "Rock":
            print("You lose...", player_1, "smashes", player_2)
        else:
            print("You win!", player_2, "cut", player_1)
    else:
        print("That's not a valid play. Check your spelling!")
    #player_2 was set to True, but we want it to be False so the loop continues
    player_2 = False
    player_1 = n[randint(0,2)] #in this case, player_1 is the computer which is why it's random!