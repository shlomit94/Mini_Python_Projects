name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, its has come to an end and you can go left or right. which way would you like to go? ").lower()

if answer == "left":
    answer = input("You came to a river, you can walk around it or swin across? type walk to walk around and swim to swim across: ").lower()
    
    if answer == "swim":
        print("You swam across and were eaten by alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose.")
    
elif answer == "right":
    answer = input("You came to a bridge, its looks wobbly, do you want to cross it or head back (cross/back)? ").lower()
    
    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ").lower()
        
        if answer == "yes":
            print("You talk to the stranger and they give you a gold.")
            
        elif answer == "no":
            print("You ignored the stranger and they got offended. You lose.") 
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose.")
    
print("Thank you for trying", name)