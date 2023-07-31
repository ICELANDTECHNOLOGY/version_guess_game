import random

secret_number = 5

random_number = random.randint(0, secret_number)
guesses = 0
print("please enter between 0 and 6")


while True:
    guesses += 1
    your_guess = input("Make a guess: ")
    if your_guess.isdigit():
     your_guess= int(your_guess)
    else:
       print("type a number next time") 
       continue
    if your_guess == secret_number:
       print("YOU WON!")
       break
    else:
       print("YOU LOSE!")

print( "you won in", guesses, "guesses")