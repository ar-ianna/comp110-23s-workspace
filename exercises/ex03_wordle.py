"""EX03 - Structured Wordle"""
__author__ = "730488361"


def contains_char(word: str, letter: str) -> bool:
    """Returns if letter is at any index of word or not"""
    word_idx: int = 0
    assert len(letter) == 1
    while word_idx < len(word):
        if letter == word[word_idx]:
            return True
        word_idx = word_idx + 1
    return False

def emojified (guess: str, secret: str) -> str:
    """When guess & secret are equal length, corresponding emojis will be produced"""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(guess) == len(secret)
    guess_idx: int = 0
    emojis: str = ""
    while guess_idx < len(guess):
        if guess[guess_idx] == secret[guess_idx]:
            emojis += GREEN_BOX
        elif contains_char(secret, guess[guess_idx])== True:
            emojis += YELLOW_BOX
        else:
            emojis += WHITE_BOX
        guess_idx = guess_idx + 1
    return emojis

def input_guess(expected_length: int) -> str:
    """Prompt user for valid guess"""
    guess: str = str(input(f"Enter a {expected_length} character word: "))
    while len(guess) != expected_length:
        try_again: str = str(input(f"That was not {expected_length} chars! Try again: ")) 
        guess = try_again
    return guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turns_taken: int = 1
    while turns_taken <= 6:
        print(f"=== Turn {turns_taken}/6 ===")
        guess: input_guess(len(secret))
        if guess == secret:
            print(emojified(guess, secret))
            print(f"You won in {turns_taken}/6 turns!")
        if guess != secret:
            print(emojified(guess, secret))
            turns_taken += 1
        if turns_taken > 6:
            print(emojified(guess, secret))
            print(f"X/6 - Sorry, try again tomorrow!")

