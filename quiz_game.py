print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")
score = 0

if playing.lower() != "yes":
    quit()
    
print("Okay! Let's play :)")

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")
       
answer = input("What does GPU stand for? ").lower()
print(answer)
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")
        
answer = input("What does RAM stand for? ").lower()
print(answer)

if answer == "random access memory":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")
      
answer = input("What does PSU stand for? ").lower()
if answer == "power suplly":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")
    
numOfQst = 4

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / numOfQst) * 100) + "%.")