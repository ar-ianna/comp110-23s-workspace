"""EX02 - One-Shot Wordle - Loops!"""
__author__ = "730488361"

secret: str = "python"
guess: str = str(input(f"What is your 6-letter guess?"))
playing: bool = True

word_idx = int = 0
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

e_1: str = GREEN_BOX or WHITE_BOX or YELLOW_BOX
e_2: str = GREEN_BOX or WHITE_BOX or YELLOW_BOX
e_3: str = GREEN_BOX or WHITE_BOX or YELLOW_BOX
e_4: str = GREEN_BOX or WHITE_BOX or YELLOW_BOX
e_5: str = GREEN_BOX or WHITE_BOX or YELLOW_BOX
e_6: str = GREEN_BOX or WHITE_BOX or YELLOW_BOX

more_opt: str = secret[len(secret) - 6] or secret[len(secret) - 5] or secret[len(secret) - 4] or secret[len(secret) - 3] or secret[len(secret) - 2] or secret[len(secret) - 1] 

while playing: 
    if len(guess) != len(secret):
        try_again: str = str(input(f"That was not 6 letters! Try again: ")) 
        guess = try_again
    else:
        if len(guess) == len(secret):
            if guess == secret:
                if word_idx < len(secret):
                    if word_idx == 0:
                        if guess[len(guess) - 6] == secret[len(secret) - 6]:
                            e_1: str = GREEN_BOX
                        else:
                            if guess[len(guess) - 6] != secret[len(secret) - 6]:
                                e_1: str = WHITE_BOX
                        word_idx = word_idx + 1
                    if word_idx == 1:
                        if guess[len(guess) - 5] == secret[len(secret) - 5]:
                            e_2: str = GREEN_BOX
                        else:
                            if guess[len(guess) - 5] != secret[len(secret) - 5]:
                                e_2: str = WHITE_BOX
                        word_idx = word_idx + 1
                    if word_idx == 2:
                        if guess[len(guess) - 4] == secret[len(secret) - 4]:
                            e_3: str = GREEN_BOX
                        else:
                            if guess[len(guess) - 4] != secret[len(secret) - 4]:
                                e_3: str = WHITE_BOX
                        word_idx = word_idx + 1
                    if word_idx == 3:
                        if guess[len(guess) - 3] == secret[len(secret) - 3]:
                            e_4: str = GREEN_BOX
                        else:
                            if guess[len(guess) - 3] != secret[len(secret) - 3]:
                                e_4: str = WHITE_BOX
                        word_idx = word_idx + 1
                    if word_idx == 4:
                        if guess[len(guess) - 2] == secret[len(secret) - 2]:
                            e_5: str = GREEN_BOX
                        else:
                            if guess[len(guess) - 2] != secret[len(secret) - 2]:
                                e_5: str = WHITE_BOX
                        word_idx = word_idx + 1
                    if word_idx == 5:
                        if guess[len(guess) - 1] == secret[len(secret) - 1]:
                            e_6: str = GREEN_BOX
                        else:
                            if guess[len(guess) - 1] != secret[len(secret) - 1]:
                                e_6: str = WHITE_BOX
                        word_idx = word_idx + 1
                    print(e_1 + e_2 + e_3 + e_4 + e_5 + e_6)
                    print(f"Woo! You got it!")
                    playing = False
            else:
                if guess != secret:
                    if word_idx < len(secret):
                        if word_idx == 0:
                            if guess[len(guess) - 6] == secret[len(secret) - 6]:
                                e_1 = GREEN_BOX
                            else:
                                if guess[len(guess) - 6] >= more_opt:
                                    e_1 = YELLOW_BOX
                                else: 
                                    if guess[len(guess) - 6] != more_opt:
                                        e_1 = WHITE_BOX
                            word_idx = word_idx + 1
                        if word_idx == 1:
                            if guess[len(guess) - 5] == secret[len(secret) - 5]:
                                e_2 = GREEN_BOX
                            else:
                                if guess[len(guess) - 5] >= more_opt:
                                    e_2 = YELLOW_BOX
                                else: 
                                    if guess[len(guess) - 5] != more_opt:
                                        e_2 = WHITE_BOX
                            word_idx = word_idx + 1
                        if word_idx == 2:
                            if guess[word_idx] == secret[word_idx]:
                                e_3 = GREEN_BOX
                            else:
                                if guess[len(guess) - 4] >= more_opt:
                                    e_3 = YELLOW_BOX
                                else: 
                                    if guess[len(guess) - 4] != more_opt:
                                        e_3 = WHITE_BOX
                            word_idx = word_idx + 1
                        if word_idx == 3:
                            if guess[len(guess) - 3] == secret[len(secret) - 3]:
                                e_4 = GREEN_BOX
                            else:
                                if guess[len(guess) - 3] >= more_opt:
                                    e_4 = YELLOW_BOX
                                else: 
                                    if guess[len(guess) - 3] != more_opt:
                                        e_4 = WHITE_BOX
                            word_idx = word_idx + 1
                        if word_idx == 4:
                            if guess[len(guess) - 2] == secret[len(secret) - 2]:
                                e_5 = GREEN_BOX
                            else:
                                if guess[len(guess) - 2] >= more_opt:
                                    e_5 = YELLOW_BOX
                                else: 
                                    if guess[len(guess) - 2] != more_opt:
                                        e_5 = WHITE_BOX
                            word_idx = word_idx + 1
                        if word_idx == 5:
                            if guess[len(guess) - 1] == secret[len(secret) - 1]:
                                e_6 = GREEN_BOX
                            else:
                                if guess[len(guess) - 1] >= more_opt:
                                    e_6 = YELLOW_BOX
                                else: 
                                    if guess[len(guess) - 1] != more_opt:
                                        e_6 = WHITE_BOX
                            word_idx = word_idx + 1
                        print(e_1 + e_2 + e_3 + e_4 + e_5 + e_6)
                        print("Not quite. Play again soon!")
                        playing = False  