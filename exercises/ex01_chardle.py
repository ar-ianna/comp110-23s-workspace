"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730488361"

chardle_guess: str = input("Enter a 5-character word: ")
if len(chardle_guess)==5:
    character_search: str= input("Enter a single character: ")
    if len(character_search)==1:
        print("Searching for " + character_search + " in " + chardle_guess)  
else:
    len(chardle_guess)!=5
    print("Error: Word must contain 5 characters")
    exit()
if len(character_search)!=1:
        print("Error: Character must be a single character.")
        exit()



if chardle_guess[len(chardle_guess)-1]==character_search:
    print(character_search + " found in index 4")
    if chardle_guess[len(chardle_guess)-2]==character_search:
        print(character_search + " found in index 3")
        if chardle_guess[len(chardle_guess)-3]==character_search:
            print(character_search + " found in index 2")
            if chardle_guess[len(chardle_guess)-4]==character_search:
                print(character_search + " found in index 1")
                if chardle_guess[len(chardle_guess)-5]==character_search:
                    print(character_search + " found in index 0")
                    print("5 instances of " + character_search + " found in " + chardle_guess)
                    
else:
    if chardle_guess[len(chardle_guess)-2]==character_search:
        print(character_search + " found in index 3")
        if chardle_guess[len(chardle_guess)-3]==character_search:
            print(character_search + " found in index 2")
            if chardle_guess[len(chardle_guess)-4]==character_search:
                print(character_search + " found in index 1")
                if chardle_guess[len(chardle_guess)-5]==character_search:
                    print(character_search + " found in index 0")
                    print("4 instances of " + character_search + " found in " + chardle_guess)
    else:
        if chardle_guess[len(chardle_guess)-3]==character_search:
            print(character_search + " found in index 2")
            if chardle_guess[len(chardle_guess)-4]==character_search:
                print(character_search + " found in index 1")
                if chardle_guess[len(chardle_guess)-5]==character_search:
                    print(character_search + " found in index 0")
                    ("3 instances of " + character_search + " found in " + chardle_guess)
        else:
            if chardle_guess[len(chardle_guess)-4]==character_search:
                print(character_search + " found in index 1")
                if chardle_guess[len(chardle_guess)-5]==character_search:
                    print(character_search + " found in index 0")
                    ("2 instances of " + character_search + " found in " + chardle_guess)
            else:
                if chardle_guess[len(chardle_guess)-5]==character_search:
                    print(character_search + " found in index 0")
                    ("1 instances of " + character_search + " found in " + chardle_guess)
                else:
                    if chardle_guess[len(chardle_guess)-5]!=character_search:
                        print("No instances of " + character_search + " found in " + chardle_guess)