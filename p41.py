import random
def guess_the_number():
    number_to_guess = random.randint(1, 10)
    attempts = 0
    guess = None
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 10.")
    print("Can you guess what it is?")
    while guess != number_to_guess:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the correct number: {number_to_guess}")
                print(f"It took you {attempts} attempts to guess the number.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
if __name__ == "__main__":
    guess_the_number()
