"""EX06 - Choose Your Own Adventure!"""
___author___ = "730488361"

points: int = 0
player: str = ""
EVIL: str = "\U0001f608"
GOOD: str = "\U0001f607"
ROBOT: str = "\U0001f916"


def main() -> None:
    """Entrypoint to the quiz!"""
    global points
    greet()
    option: str = str(input("This part is on you. If you're a human of many words, pick 1, if you're few on words but bigger on numbers, pick 2, or if you're over this whole process already, pick 3: "))
    if option == "1":
        choice_1()
        result()
    else:
        if option == "2":
            points = choice_2(points)
            result()
        else: 
            if option == "3":
                choice_3()


def greet() -> None:
    """Player greeting!"""
    player = str(input("Woah...Who are you?"))
    print(f"Greetings {player}. Are you on the side of good {GOOD} or evil {EVIL}? Take this quiz to see what type of Transformer you are! {ROBOT}")


def choice_1() -> None:
    """Good vs Evil."""
    good: str = "good"
    evil: str = "evil"
    global points
    choice: str = str(input("Let's just get this off your chest. Are you good or evil?:"))
    if good in choice:
        print(f"Thats good to hear {player}, but we need to be sure.")
        points += 1 
    elif evil in choice:
        print(f"But are you really evil {player}? Let's find out.")
        points -= 1
    else:
        print(f"Not sure {player}? That's fine, becuase we're about to find out.")
        points += 0 
    game_loop()


def choice_2(x: int) -> int:
    """Range of Good & Evil."""
    game_loop()
    new_points: int = x
    print(f"Well {player}, it's time for a numerical analysis straight from Cybertron!")
    y: int = int(input("Say you had $100 - How many dollars would you give to someone that is homeless?:"))
    if y >= 1:
        new_points += 1
    return new_points


def choice_3() -> None:
    """Exit the quiz!"""
    print(f"Well {player}, it was nice to meet you, & no matter what anyone says you'll always be a pretty good human in my eyes.")
    print(f"{points} points accumulated")


def game_loop() -> None:
    """Mini Quiz!"""
    global points
    print(f"Time to get to the good stuff {player} with some yes or no questions!")
    q1: str = str(input("QUESTION 1! Do you like pineapple on pizza?:"))
    if q1 == "yes":
        points += 1
    else:
        if q1 == "no":
            points -= 1
    print("Interesting...")
    q2: str = str(input("QUESTION 2! Do you like puppies?"))
    if q2 == "yes":
        points += 1
    else:
        if q2 == "no":
            points -= 1
    print("Hmmm....")
    q3: str = str(input("QUESTION 3! What about kittens?"))
    if q3 == "yes":
        points += 1
    else:
        if q3 == "no":
            points -= 1
    print("Noted....")
    

def result() -> None:
    """Autobot or Decepticon."""
    global points
    from random import randint
    x: int = randint(1, 100)
    if points >= 2:
        print(f"{player}....you are an Autobot {GOOD}! The {x} one we've seen today!")
        print(f"{points} points accumulated")
    else:
        print(f"{player}....you are a Decepticon {EVIL}! The {x} one we've seen today!")
        print(f"{points} points accumulated")


if __name__ == "__main__":
    main()