numtries = 0
lives = 20
import random
correct = random.randint(1,20)
for lives in range(20):
    numtries = numtries + 1 
    print("Guess a number between 1-200")
    lives = str(20-lives)
    guess = input("You have " + lives + " live(s) left: ")
    numguess = int(guess)
    if (numguess == correct): 
        str_tries =  str(numtries) 
        print("Well done!")
        print("You have solved the problem in " + str_tries + " tries.") 
        lives = 20
    else:
        if (numguess > correct): 
            print("Wrong! Too high.")
        else:
            print("Wrong! Too low.")
if numguess != correct:
    print("oops! you ran out of lives")
