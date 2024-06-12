import random

def stage_1():
    print("Welcome to Stage 1!")
    print("You have 5 guesses to guess the number between 1 and 25.")
    print("Good luck!")
    random_number = random.randint(1, 25)
    num_guesses = 0

    while num_guesses < 5:
        try:
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > 25:
                print("Please enter a number between 1 and 25.")
                continue

            num_guesses += 1

            if guess == random_number:
                print(f"Congratulations! You guessed the number in {num_guesses} guesses.")
                break
            elif guess < random_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Please enter a valid number.")

    if num_guesses == 5 and guess != random_number:
        print(f"Sorry, you ran out of guesses. The number was {random_number}.")

if __name__ == "__main__":
    stage_1()