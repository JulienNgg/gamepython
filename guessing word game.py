import random

def choose_word():
    words = ["python", "programming", "hangman", "computer", "science", "developer", "challenge"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman_game():
    print("Welcome to Hangman!")
    secret_word = choose_word()
    guessed_letters = []
    attempts = 6  # Number of incorrect attempts allowed

    while attempts > 0:
        print("\n" + display_word(secret_word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            attempts -= 1
            print(f"Incorrect! Attempts left: {attempts}")
        
        if set(guessed_letters) == set(secret_word):
            print("Congratulations! You guessed the word:", secret_word)
            break

    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The correct word was: {secret_word}")

if __name__ == "__main__":
    hangman_game()
