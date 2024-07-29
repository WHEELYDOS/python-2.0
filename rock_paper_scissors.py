#it is a rock paper scissor game 
play_again = True
while play_again is True:
    import random

    choices = ["rock" , "paper" , "scissors"]

    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = str(input("enter your choice - ").lower())

    print("computer- " + computer   )
    print("player- " + player)

    if player == computer:
        print("tie")

    elif player == "rock" and computer== "scissors":
        print("player wins")

    elif player != "rock" and computer == "scissors":
        print("computer wins")

    elif player == "rock" and computer== "scissors":
        print("player wins")

    else :
        print ("computer wins")

    play_again = input(" do you want to play again ? (y/n) " ).lower()
    if play_again != "y":
        play_again=False

print("bye bye ")