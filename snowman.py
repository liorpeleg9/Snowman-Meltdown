import random

WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word() -> str:
    """Select a random word from the list."""
    return random.choice(WORDS)


def play_game() -> None:
    """Run the Snowman Meltdown starter loop."""
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected:", secret_word)  # for testing only

    guess = input("Guess a letter: ").lower()
    print("You guessed:", guess)


if __name__ == "__main__":
    play_game()
