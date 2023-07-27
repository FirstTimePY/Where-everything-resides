#Importing the random library so we can get a random choice from the computer
import random

#Creating a while loop so we can in the end ask "play again?"
while True:
    #Adding a list of choices
    choices = ["rock", "paper", "scissors"]

    #Computer will choose a random choice from the list of "choices"
    computer = random.choice(choices)

    #Player = none until they pick something
    player = None

    #Creating a loop for the players choice so they cant pick anything but the listed choices
    while player not in choices:
        player = input("rock, paper, or scissors: ").lower()

    #If the computer and player pick the same thing, its a tie
    if player == computer:
        print("Computer picks: ",computer)
        print("You picked: ",player)
        print("\nIts a tie!")

    #If the player picks rock and computer picks paper, player loses
    elif player == "rock":
        if computer == "paper":
            print("Computer picks: ",computer)
            print("You picked: ",player)
            print("\nYou lose!")    
        #If the player picks rock and computer picks scissors, player wins
        if computer == "scissors":
            print("Computer picks: ",computer)
            print("You picked: ",player)
            print("\nYou win!")   

    #If the player picks scissors and computer picks paper, player wins
    elif player == "scissors":
        if computer == "paper":
            print("Computer picks: ",computer)
            print("You picked: ",player)
            print("\nYou win!")       
        #If the player picks scissors and computer picks rock, player loses
        if computer == "rock":
            print("Computer picks: ",computer)
            print("You picked: ",player)
            print("\nYou lose!")  

    #If the player picks rock and computer picks scissors, player wins
    elif player == "rock":
        if computer == "scissors":
            print("Computer picks: ",computer)
            print("You picked: ",player)
            print("\nYou win!")    
        #If the player picks rock and computer picks paper, player loses   
        if computer == "paper":
            print("Computer picks: ",computer)
            print("You picked: ",player)
            print("\nYou lose!")

    #Finally, the play again function
    play_again = input("Play again? (y/n): ").lower()

    #If the player chooses anything but "y(yes)" we will break out of the loop
    if play_again != "y":
        break
#Print "Cya later!" after the player decides to NOT play again
print("Cya later!")


