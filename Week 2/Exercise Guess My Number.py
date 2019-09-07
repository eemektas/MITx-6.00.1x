low = 0
high = 100
guess = 50
letter = ""

print("Please think of a number between 0 and 100!")

while letter != 'c':
    print("Is your secret number " + str(guess) + "?")
    letter = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if letter != 'h' and letter != 'l' and letter != 'c':
        print("Sorry I didn't understand your input.")
    elif letter == 'h':
        high = guess
    elif letter == 'l':
        low = guess
    guess = int((high + low) / 2)

print("Game over. Your secret number was:", guess)


