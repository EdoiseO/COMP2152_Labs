import random
# Solution for Week 02 Lab
choices = ["Rock", "Paper", "Scissors"]
print(choices)

playerChoice = input("Enter a number between 1 to 3 for the following choices: 1-Rock, 2-Paper, 3-Scissors: ")

playerChoice = int (playerChoice)

if  playerChoice < 1 or playerChoice > 3:
    print("Error: Choice should be bettween 1 and 3")
else: 
    # Develop the game logic using if/elif/else
    computerChoice = random.randint(1, 3)

    if playerChoice == computerChoice:
        print("Its a choice")
    elif playerChoice == 1 and computerChoice == 3: 
        print("Rocke beats Scissors - You win!")
    elif playerChoice == 2 and computerChoice == 1: 
        print ("Paper beats Rock - You win!")
    elif playerChoice == 3 and computerChoice == 2: 
        print("Scissors beats Paper - You win!")     
    else:
        print("You lose!")    