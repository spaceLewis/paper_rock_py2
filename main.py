import random
from sub.game_logic import compare_choices

def get_computer_choice():
    choices = ['r', 'p', 's']  # Use shorthand values
    return random.choice(choices)

def play_game():
    # Provide a welcome message
    print("Welcome to the Paper Rock Scissors game!")

    # Get the user's choice
    user_choice = raw_input("Please choose either 'r' (rock), 'p' (paper), or 's' (scissors): ")

    # Get the computer's choice
    computer_choice = get_computer_choice()

    # Compare the two choices
    result = compare_choices(user_choice, computer_choice)

    # Print the results
    print("You chose %s, and the computer chose %s." % (user_choice, computer_choice))
    print(result)

    # Ask the user if they want to play again
    play_again = raw_input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_game()

    # Say goodbye and end the game
    print("Thank you for playing the Paper Rock Scissors game!")

# Call the function to start the game
play_game()
