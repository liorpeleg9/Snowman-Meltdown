import random

WORDS = ["python", "git", "github", "snowman", "meltdown"]

STAGES = [
    # Stage 0: Full snowman
    """
     ___
    /___\\
    (o o)
    ( : )
    ( : )
    """,

    # Stage 1: Bottom part starts melting
    """
     ___
    /___\\
    (o o)
    ( : )
    """,

    # Stage 2: Only the head remains
    """
     ___
    /___\\
    (o o)
    """,

    # Stage 3: Snowman completely melted
    """
     ___
    /___\\
    """
]


def get_random_word() -> str:
    """Select a random word from the list."""
    return random.choice(WORDS)

def display_game_state(mistakes: int, secret_word: str, guessed_letters: set[str]) -> None:
    """Display the current snowman stage and the guessed word."""
    print(STAGES[mistakes])

    masked_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            masked_word += letter + " "
        else:
            masked_word += "_ "

    print("Word:", masked_word.strip())
    print()


def play_game() -> None:
    """Run the Snowman Meltdown game (partial logic)."""
    secret_word = get_random_word()
    guessed_letters: set[str] = set()
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    # Display initial game state
    display_game_state(mistakes, secret_word, guessed_letters)

    guess = input("Guess a letter: ").lower()
    guessed_letters.add(guess)

    display_game_state(mistakes, secret_word, guessed_letters)



if __name__ == "__main__":
    play_game()
