import random

# Hangman stages (ASCII Art)
HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |
     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ==="""
]

# Word categories
CATEGORIES = {
    "Animals": ["tiger", "elephant", "giraffe", "kangaroo", "zebra"],
    "Fruits": ["apple", "banana", "grape", "orange", "strawberry"],
    "Countries": ["india", "canada", "brazil", "germany", "japan"]
}

def choose_word(category):
    return random.choice(CATEGORIES[category])

def display_game(word, guessed, attempts, used_letters):
    print(HANGMAN_PICS[len(HANGMAN_PICS) - 1 - attempts])
    print("\nWord: ", " ".join(guessed))
    print(f"Attempts left: {attempts}")
    print("Used letters:", " ".join(used_letters))

def play_game():
    print("🎮 Welcome to Hangman Game!")
    print("Categories: ", ", ".join(CATEGORIES.keys()))

    # Choose category
    category = input("Choose a category: ").capitalize()
    if category not in CATEGORIES:
        print("❌ Invalid category. Defaulting to 'Animals'.")
        category = "Animals"

    # Difficulty levels
    print("\nChoose difficulty level: Easy (8), Medium (6), Hard (4)")
    level = input("Enter level: ").lower()
    attempts = {"easy": 8, "medium": 6, "hard": 4}.get(level, 6)

    # Select word
    word = choose_word(category)
    guessed = ["_"] * len(word)
    used_letters = []

    # Game loop
    while attempts > 0 and "_" in guessed:
        display_game(word, guessed, attempts, used_letters)

        guess = input("\nEnter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Please enter a single alphabet.")
            continue

        if guess in used_letters:
            print("⚠️ You already guessed that letter.")
            continue

        used_letters.append(guess)

        if guess in word:
            print("✅ Correct guess!")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
        else:
            attempts -= 1
            print("❌ Wrong guess!")

    # Final result
    display_game(word, guessed, attempts, used_letters)
    if "_" not in guessed:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print("\n💀 Game Over! The word was:", word)

# Main loop
if __name__ == "__main__":
    while True:
        play_game()
        replay = input("\nDo you want to play again? (yes/no): ").lower()
        if replay != "yes":
            print("👋 Thanks for playing! Goodbye!")
            break
