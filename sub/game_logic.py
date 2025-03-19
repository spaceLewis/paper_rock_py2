def compare_choices(user_choice, computer_choice):
    # Map shorthand inputs to full names
    shorthand_map = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    user_choice = shorthand_map.get(user_choice, user_choice)
    computer_choice = shorthand_map.get(computer_choice, computer_choice)

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"
