import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word() -> str:
    """Select a random secret word."""
    return random.choice(WORDS)


def display_game_state(mistakes: int, secret_word: str, guessed_letters: set[str]) -> None:
    """Display the current snowman stage and the guessed word."""
    print(STAGES[mistakes])

    masked_word = ""
    for letter in secret_word:
        masked_word += (letter if letter in guessed_letters else "_") + " "

    print("Word:", masked_word.strip())
    print(f"Mistakes: {mistakes}/{len(STAGES) - 1}")
    if guessed_letters:
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
    print()


def get_guess(guessed_letters: set[str]) -> str:
    """Prompt the user until they enter a valid single new letter."""
    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.\n")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue
        return guess


def is_word_guessed(secret_word: str, guessed_letters: set[str]) -> bool:
    """Return True if all letters in the secret word have been guessed."""
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True


def play_game() -> None:
    """Run the Snowman Meltdown game loop and offer replay."""
    print("Welcome to Snowman Meltdown!")

    while True:
        secret_word = get_random_word()
        guessed_letters: set[str] = set()
        mistakes = 0
        max_mistakes = len(STAGES) - 1

        while True:
            display_game_state(mistakes, secret_word, guessed_letters)

            guess = get_guess(guessed_letters)
            guessed_letters.add(guess)

            if guess in secret_word:
                print("✅ Correct!\n")
                if is_word_guessed(secret_word, guessed_letters):
                    print(f"🎉 You saved the snowman! The word was '{secret_word}'.")
                    break
            else:
                mistakes += 1
                print("❌ Wrong!\n")
                if mistakes >= max_mistakes:
                    display_game_state(mistakes, secret_word, guessed_letters)
                    print(f"☠️ The snowman melted... The word was '{secret_word}'.")
                    break

        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break
        print()
