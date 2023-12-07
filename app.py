import random

def number_guessing_game():
    # Set the range for the random number
    min_num = 1
    max_num = 100
    secret_number = random.randint(min_num, max_num)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print(f"Guess the number between {min_num} and {max_num}")

    while True:
        guess = input("Enter your guess (or 'exit' to quit): ")

        if guess.lower() == 'exit':
            print("Goodbye! Thanks for playing.")
            break

        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number or 'exit' to quit.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try guessing a higher number.")
        elif guess > secret_number:
            print("Too high! Try guessing a lower number.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
            break

if __name__ == "__main__":
    number_guessing_game()