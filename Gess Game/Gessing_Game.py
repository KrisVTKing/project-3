from stage_1 import stage_1
from stage_2 import stage_2
from stage_3 import stage_3
from stage_4 import stage_4
from stage_5 import stage_5
def main_menu():
    print("Welcome to MyGuessing Game!")
    print("Progress through increasingly challenging stages by guessing the secret number within a limited number of tries.")
    print("Can you conquer all five stages?")
    print("\nDisclaimer: The progress is not saved. You need to track your progress yourself.")
    print("Good luck!")
    while True:
        user_input = input("Please select an option: \n1. Stage 1: Novice Numbers,\n2. Stage 2: Beginner's Luck,\n3. Stage 3: Intermediate Insight,\n4. Stage 4: Advanced Accuracy,\n5. Stage 5: Expert Estimation,\n6. Exit: \n")
        if user_input.isdigit():
            user_input = int(user_input)
            if user_input == 1:
                stage_1()
            elif user_input == 2:
                stage_2()
            elif user_input == 3:
                stage_3()
            elif user_input == 4:
                stage_4()
            elif user_input == 5:
                stage_5()
            elif user_input == 6:
                print("Goodbye!")
                break
            else:
                print("Invalid input. Please select a number between 1 and 6.")
        else:
            print("Invalid input. Please enter a number.")
if __name__ == "__main__":
    main_menu()