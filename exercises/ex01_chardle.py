"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730488361"

chardle_guess: str = input("Enter a 5-character word: ")
if len(chardle_guess) == 5:
    character_search: str= input("Enter a single character: ")
    if len(character_search) == 1:
        print("Searching for " + character_search + " in " + chardle_guess) 
else:
    len(chardle_guess)!= 5
    print("Error: Word must contain 5 characters")
    exit()
if len(character_search)!=1:
        print("Error: Character must be a single character.")
        exit()
frequency: int = 0
if chardle_guess[len(chardle_guess) - 1] == character_search:
    print(character_search + " found at index 4")
    frequency + 1 
if chardle_guess[len(chardle_guess) - 2] == character_search:
    print(character_search + " found at index 3")
    frequency + 1
if chardle_guess[len(chardle_guess) - 3] == character_search:
    print(character_search + " found at index 2")
    frequency + 1
if chardle_guess[len(chardle_guess) - 4] == character_search:
    print(character_search + " found at index 1")
    frequency + 1
if chardle_guess[len(chardle_guess) - 5] == character_search:
    print(character_search + " found at index 0")
    frequency + 1


print (frequency)