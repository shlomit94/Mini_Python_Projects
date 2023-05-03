import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    print(user_input)
    if user_input == "q":
        print("You quit the game")
        break
        
    if user_input not in options:
        print("Unvalid option")
        continue
    
    random_number = random.randint(0, 2)
    # rock: 0 , paper: 1, scissors: 2
    compuer_pick = options[random_number]
    print("Computer picked", compuer_pick + ".")
    
    if user_input == "rock" and compuer_pick == "scissors":
        print("You won!")
        user_wins += 1
    
    elif user_input == "paper" and compuer_pick == "rock":
        print("You won!")
        user_wins += 1
    
    elif user_input == "scissors" and compuer_pick == "paper":
        print("You won!")
        user_wins += 1
        
    else:
        print("You lost!")
        computer_wins += 1
        
print("You won", user_wins, "times.") 
print("The computer won", computer_wins, "times.")
print("Goodbye!")