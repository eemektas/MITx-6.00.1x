def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    print("-----------")
    lettersGuessed = []
    guess = 8

    while guess > 0:
        print("You have", guess, "guesses left.")
        print("Available letters:", getAvailableLetters(lettersGuessed))
        letter = input("Please guess a letter: ")
        letter = letter.lower()
        if letter in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
        elif letter in secretWord:
            lettersGuessed.append(letter)
            print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
        elif letter not in secretWord:
            lettersGuessed.append(letter)
            print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
            guess -= 1
        print("-----------")
        if isWordGuessed(secretWord, lettersGuessed):
            print("Congratulations, you won!")
            break
    if guess == 0:
        print("Sorry, you ran out of guesses. The word was else.")