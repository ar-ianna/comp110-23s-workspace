"""EX02 - One-Shot Wordle - Loops!"""
__author__ = "730488361"

SECRET: str = "python"
guess: str = str(input("What is your 6-letter guess?"))
playing: bool = True

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

word_idx: int = 0
emoji_1: str = GREEN_BOX or WHITE_BOX
emoji_2: str = GREEN_BOX or WHITE_BOX
emoji_3: str = GREEN_BOX or WHITE_BOX
emoji_4: str = GREEN_BOX or WHITE_BOX
emoji_5: str = GREEN_BOX or WHITE_BOX
emoji_6: str = GREEN_BOX or WHITE_BOX

while playing: 
    if len(guess) != 6:
        print("That was not 6 letters! Try again: ")
        guess = str = str(input("What is your 6-letter guess? "))
    else:
        if len(guess) == 6:
            if guess == SECRET:
                if word_idx <= len(SECRET):
                    if word_idx == 0:
                        if guess[len(guess)-6] == SECRET[len(SECRET)-6]:
                            emoji_1: str = GREEN_BOX
                        else:
                            if guess[len(guess)-6] != SECRET[len(SECRET)-6]:
                                emoji_1: str = WHITE_BOX
                        word_idx = word_idx + 1
                    if word_idx == 1:
                        if guess[len(guess)-5] == SECRET[len(SECRET)-5]:
                            emoji_2: str = GREEN_BOX
                        else:
                            if guess[len(guess)-5] != SECRET[len(SECRET)-5]:
                                emoji_2: str = WHITE_BOX
                        word_idx = word_idx + 1
                    if word_idx == 2:
                        if guess[len(guess)-4] == SECRET[len(SECRET)-4]:
                            emoji_3: str = GREEN_BOX
                        else:
                            if guess[len(guess)-4] != SECRET[len(SECRET)-4]:
                                emoji_3: str = WHITE_BOX
                        word_idx = word_idx + 1
                    if word_idx == 3:
                        if guess[len(guess)-3] == SECRET[len(SECRET)-3]:
                            emoji_4: str = GREEN_BOX
                        else:
                            if guess[len(guess)-3] != SECRET[len(SECRET)-3]:
                                emoji_4: str = WHITE_BOX
                        word_idx = word_idx + 1
                    if word_idx == 4:
                        if guess[len(guess)-2] == SECRET[len(SECRET)-2]:
                            emoji_5: str = GREEN_BOX
                        else:
                            if guess[len(guess)-2] != SECRET[len(SECRET)-2]:
                                emoji_5: str = WHITE_BOX
                        word_idx = word_idx + 1
                    if word_idx == 5:
                        if guess[len(guess)-1] == SECRET[len(SECRET)-1]:
                            emoji_6: str = GREEN_BOX
                        else:
                            if guess[len(guess)-1] != SECRET[len(SECRET)-1]:
                                emoji_6: str = WHITE_BOX
                        word_idx = word_idx + 1
                    print(emoji_1 + emoji_2 + emoji_3 + emoji_4 + emoji_5 + emoji_6)
                    print("Woo! You got it!")
                    playing = False
            else:
                if guess != SECRET:
                    if word_idx <= len(SECRET):
                        if word_idx == 0:
                            if guess[len(guess)-6] == SECRET[len(SECRET)-6]:
                                emoji_1: str = GREEN_BOX
                            else:
                                if guess[len(guess)-6] == SECRET[len(SECRET)-6] or SECRET[len(SECRET)-5] or SECRET[len(SECRET)-3] or SECRET[len(SECRET)-2] or SECRET[len(SECRET)-1]:
                                    emoji_1: str = YELLOW_BOX
                                else:
                                    emoji_1: str = WHITE_BOX
                            word_idx = word_idx + 1
                        if word_idx == 1:
                            if guess[len(guess)-5] == SECRET[len(SECRET)-5]:
                                emoji_2: str = GREEN_BOX
                            else:
                                if guess[len(guess)-5] == SECRET[len(SECRET)-6] or SECRET[len(SECRET)-5] or SECRET[len(SECRET)-3] or SECRET[len(SECRET)-2] or SECRET[len(SECRET)-1]:
                                    emoji_2: str = YELLOW_BOX
                                else:
                                    emoji_2: str = WHITE_BOX
                            word_idx = word_idx + 1
                        if word_idx == 2:
                            if guess[len(guess)-4] == SECRET[len(SECRET)-4]:
                                emoji_3: str = GREEN_BOX
                            else:
                                if guess[len(guess)-4] == SECRET[len(SECRET)-6] or SECRET[len(SECRET)-5] or SECRET[len(SECRET)-3] or SECRET[len(SECRET)-2] or SECRET[len(SECRET)-1]:
                                    emoji_3: str = YELLOW_BOX
                                else:
                                    emoji_3: str = WHITE_BOX
                            word_idx = word_idx + 1
                        if word_idx == 3:
                            if guess[len(guess)-3] == SECRET[len(SECRET)-3]:
                                emoji_4: str = GREEN_BOX
                            else:
                                if guess[len(guess)-3] == SECRET[len(SECRET)-6] or SECRET[len(SECRET)-5] or SECRET[len(SECRET)-3] or SECRET[len(SECRET)-2] or SECRET[len(SECRET)-1]:
                                    emoji_4: str = YELLOW_BOX
                                else:
                                    emoji_4: str = WHITE_BOX
                            word_idx = word_idx + 1
                        if word_idx == 4:
                            if guess[len(guess)-2] == SECRET[len(SECRET)-2]:
                                emoji_5: str = GREEN_BOX
                            else:
                                if guess[len(guess)-2] == SECRET[len(SECRET)-6] or SECRET[len(SECRET)-5] or SECRET[len(SECRET)-3] or SECRET[len(SECRET)-2] or SECRET[len(SECRET)-1]:
                                    emoji_5: str = YELLOW_BOX
                                else:
                                    emoji_5: str = WHITE_BOX
                            word_idx = word_idx + 1
                        if word_idx == 5:
                            if guess[len(guess)-1] == SECRET[len(SECRET)-1]:
                                emoji_6: str = GREEN_BOX
                            else:
                                if guess[len(guess)-1] == SECRET[len(SECRET)-6] or SECRET[len(SECRET)-5] or SECRET[len(SECRET)-3] or SECRET[len(SECRET)-2] or SECRET[len(SECRET)-1]:
                                    emoji_6: str = YELLOW_BOX
                                else:
                                    emoji_6: str = WHITE_BOX
                            word_idx = word_idx + 1
                        print(emoji_1 + emoji_2 + emoji_3 + emoji_4 + emoji_5 + emoji_6)
                        print("Not quite. Play again soon!")
                        playing = False  

        