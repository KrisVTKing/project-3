import random

def stage_3():
    print("Welcome to Stage 3!")
    print("You have 7 guesses to guess the number between 1 and 75.")
    print("Good luck!")
    random_number = random.randint(1, 75)
    num_guesses = 0

    while num_guesses < 7:
        try:
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > 75:
                print("Please enter a number between 1 and 75.")
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

    if num_guesses == 7 and guess != random_number:
        print(f"Sorry, you ran out of guesses. The number was {random_number}.")

if __name__ == "__main__":
    stage_3()