#Pritam Raj Rajbanshi
#Ratespiel

import random
randomNumber = random.randrange(0,100)  
print("Random number has been generated")
guessed = False
while guessed==False:
    userInput = int(input("Please input a number between 0 and 100: "))
    if userInput==randomNumber:
        guessed = True
        print("congratulations!🎉")
    elif userInput>randomNumber:
        print("Your guess is too high: please try a number lower")
    elif userInput < randomNumber:
        print("Your guess is too low: please try a number higher")

