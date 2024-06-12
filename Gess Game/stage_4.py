import random

def stage_4():
    print("Welcome to Stage 4!")
    print("You have 8 guesses to guess the number between 1 and 100.")
    print("Good luck!")
    random_number = random.randint(1, 100)
    num_guesses = 0

    while num_guesses < 8:
        try:
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
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
    
    if num_guesses == 8 and guess != random_number:
        print(f"Sorry, you ran out of guesses. The number was {random_number}.")

if __name__ == "__main__":
    stage_4()