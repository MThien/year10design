numtries = 0
lives = 0
import random
correct = random.randint(1,200)
#randomizes the correct number every time from 1-200
bottom = str(1)
restart = True
top = str(200)
#set bottom and top numbers
print("Guess a number between " + bottom + " - " + top + ". You have 10 lives")
while restart == True: 
    while lives<11:
        numtries = numtries + 1
        showlives = str(10-lives)
        guess = input("You have " + showlives + " live(s) left: ")
        if (guess.isdigit()):
            numguess = int(guess)
            if (numguess == correct): 
                str_tries =  str(numtries) 
                print("Well done!")
                print("You have solved the problem in " + str_tries + " tries.")
                print("You did it!!!")
                x=input("do you want to restart? yes or no? ")
                if x == "yes":
                    restart == True
                    lives = 0
                    bottom = str(1)
                    top = str(200)
                    correct = random.randint(1,200)
                else:
                    exit()
            else:
                if (numguess > correct):
                    if (numguess < int(top)):
                        top = str(numguess)
                        print("Guess a number between " + bottom + " - " + top)
                        lives=lives+1
                    else:
                        print("Guess a number between " + bottom + " - " + top)
                        lives=lives+1
                else:
                    if (numguess > int(bottom)):  
                        bottom = str(numguess)
                        print("Guess a number between " + bottom + " - " + top)
                        lives=lives+1
                    else:
                        print("Guess a number between " + bottom + " - " + top)
                        lives=lives+1
                if (numguess - correct > 0):
                    if abs(numguess - correct <=5):
                        print("ON FIRE!!! SUPER CLOSE... you are within 5 digits")
                        
        
                        
            
        else:
            print("THATS NOT A NUMBER SILLY")
    print("oops! you ran out of lives" + ". The answer was: " + str(correct))
    exit()
