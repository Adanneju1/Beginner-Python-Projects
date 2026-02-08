# This program checks how you are feeling
print("WELCOME TO THE MOOD CHECKER!")
print("How are you feeling today?")
# These are the options that give the user a chance to pick from the emotions or even think of their own
print("Here are your options:", "Happy,", "Angry,", "Sad,", "Tired,", "or", "etc!")

mood = input("Enter a mood: ") # The generated input for the user

print(" ") # Giving a space between the prompt question and the reponse that the user can recieve

# If statement options: if user added in one of the options!
if mood == "Happy":
    print("😊 That's awesome! I'm glad you're feeling happy today!")

elif mood == "Sad":
    print("💙 I'm sorry you're feeling sad. I hope things get better.")

elif mood == "Angry":
    print("😤 That sounds rough. Take a deep breath—you've got this.")

elif mood == "Tired":
    print("😌 Thanks for sharing how you feel. Take care of yourself today.")

else:
    print("🤔 I don't recognize that mood, but thanks for sharing.")
