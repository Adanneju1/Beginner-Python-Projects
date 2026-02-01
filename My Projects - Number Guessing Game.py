import random # Using this to signify that it'll be a random method used in this python coding taking place!

secret_number = random.randint(1, 10) # The randomizer for the value assigned to the sceret_number, identifier
guess = int(input("Guess a number between 1 and 10: ")) # The number, the user could type in

while guess != secret_number: # A "While" loop for when we know where to stop
    if guess < secret_number: # a condition if the number is to low
        print("Too low!")
    elif guess > secret_number: # a condition if the number is to high!
        print("Too high!")

    guess = int(input("Guess again: ")) # Tells user to type a different nunber!
    

print("Correct!") # finally guessed the correct number!







































    # Did the above on my own, not that bad, but not that good either

# NEED TO PUT A WHILE LOOP SOME KIND OF FORMULA LIKE WHILE =+ OR SOMETHING

# Have to put in a while loop, so that every number can have the chance to run


# Office hours wednesday and tutor on thursday

# try to pratice hands on everyday for 30 mins?! ID/k fuck everyone
