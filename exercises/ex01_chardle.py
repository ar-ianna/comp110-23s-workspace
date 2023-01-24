"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730488361"

chardle_guess: str = input("Enter a 5-character word: ")
if len(chardle_guess) == 5:
    character_search: str = input("Enter a single character: ")
    if len(character_search) == 1:
        print("Searching for " + character_search + " in " + chardle_guess) 
else:
    len(chardle_guess) != 5
    print("Error: Word must contain 5 characters")
    exit()
if len(character_search) != 1:
    print("Error: Character must be a single character.")
    exit()
frequency: int = 0

if chardle_guess[len(chardle_guess) - 1] == character_search:
    print(character_search + " found at index 4")
    frequency = frequency + 1 
if chardle_guess[len(chardle_guess) - 2] == character_search:
    print(character_search + " found at index 3")
    frequency = frequency + 1
if chardle_guess[len(chardle_guess) - 3] == character_search:
    print(character_search + " found at index 2")
    frequency = frequency + 1
if chardle_guess[len(chardle_guess) - 4] == character_search:
    print(character_search + " found at index 1")
    frequency = frequency + 1
if chardle_guess[len(chardle_guess) - 5] == character_search:
    print(character_search + " found at index 0")
    frequency = frequency + 1
if frequency == 0:
    print("No instances of " + character_search + " found in " + chardle_guess)
else: 
    if frequency == 1:
        print("1 instance of " + character_search + " found in " + chardle_guess)
if frequency > 1:
    print(str(frequency) + " instances of " + character_search + " found in " + chardle_guess)