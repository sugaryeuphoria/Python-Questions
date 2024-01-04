from random import randint


def get_user_choice():
    # Get the user choice
    user_choice = input("Enter your choice (rock, paper, or scissors): ")

    # Limiting the user choice to rock, paper, scissors, using while loop
    while user_choice.lower() not in ["rock", "paper", "scissors"]:
        user_choice = input(
            "Wrong choice. Enter your choice (rock, paper, or scissors): ")
    # Return the value entered by the user
    return user_choice.lower()


def generate_computer_choice():
    # Generating random number between 1 to 3
    computer_choice = randint(1, 3)

    # Using the random number to generate the computer choice
    if (computer_choice == 1):
        computer_choice = "rock"
    elif (computer_choice == 2):
        computer_choice = "paper"
    elif (computer_choice == 3):
        computer_choice = "scissors"
    else:
        print("Error")

    # Return the computer choice
    return computer_choice.lower()

# Writing a function to determine the winner


def determine_winner(user_choice, computer_choice):
    # If the choice of the computer and user is the same then it's a tie
    if (user_choice == computer_choice):
        return("It's a tie!")
    # Condition for Rock beats scissors
    elif (user_choice == "rock"):
        if (computer_choice == "paper"):
            return("Computer wins!")
        else:
            return("You win!")
    # Condition for scissors beats paper
    elif (user_choice == "paper"):
        if (computer_choice == "scissors"):
            return("Computer wins!")
        else:
            return("You win!")
    # Condition for paper beats rock
    elif (user_choice == "scissors"):
        if (computer_choice == "rock"):
            return("Computer wins!")
        else:
            return("You win!")

# The function that triggers the game


def main():
    user_wins = 0
    computer_wins = 0
    print("Welcome to Rock-Paper-Scissors game!")
    print("========================")
    while True:
        user_choice = get_user_choice()
        computer_choice = generate_computer_choice()
        print(f"Computer chose: {computer_choice}")
        winner = determine_winner(user_choice, computer_choice)
        if winner == "Computer wins!":
            print(winner)
            computer_wins += 1
        elif winner == "You win!":
            print(winner)
            user_wins += 1
        
        print("Current Scores: ")
        print(f"User: {user_wins}")
        print(f"Computer: {computer_wins}")
        print("========================")
        play_again = input("Play again? press any key to continue, or enter 'q' to quit: ")
        if (play_again.lower() == "q"):
            break
        else:
            continue

    print("Final Scores: ")
    print(f"User: {user_wins}")
    print(f"Computer: {computer_wins}")
    print("Thank you for playing the game!!!")

main()
