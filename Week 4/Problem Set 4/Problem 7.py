def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.

        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    while True:
        letter = input("Enter n to deal a new hand, r to replay the last hand, or e to end the game: ")
        if letter == "e":
            break
        elif letter == "r":
            try:
                if isinstance(hand, dict):
                    who = input("Enter u to have yourself play, c to have the computer play: ")
                    if who == "u":
                        playHand(hand, wordList, n)
                    elif who == "c":
                        compPlayHand(hand, wordList, n)
                    else:
                        print("Invalid command.")
            except:
                print("You have not played a hand yet. Please play a new hand first!")
        elif letter == "n":
            n = HAND_SIZE
            hand = dealHand(n)
            while True:
                who = input("Enter u to have yourself play, c to have the computer play: ")
                if who == "c":
                    compPlayHand(hand, wordList, n)
                    break
                elif who == "u":
                    playHand(hand, wordList, n)
                    break
                else:
                    print("Invalid command.")
        else:
            print("Invalid command.")