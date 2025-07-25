import random

def determine_winner(user_option, computer_option):
    if user_option == computer_option:
        return "tie"
    elif (user_option == 'rock' and computer_option == 'scissors') or \
         (user_option == 'paper' and computer_option == 'rock') or \
         (user_option == 'scissors' and computer_option == 'paper'):
        return "win"
    else:
        return "lose"

def play_game():
    while True:
        print("Welcome to Rock Paper Scissors! Merged conflict!")
        print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")
        print("Enter your choice: 'rock', 'paper', or 'scissors'. Type 'exit' to quit the game.")
        
        options = ['rock', 'paper','scissors']
              
        user_option = input("Your option is: ").lower()

        if user_option == 'exit':
            print("Thanks for playing! Goodbye!")
            break         

        if user_option not in options:
            print('Please choose a correct option: rock, paper, scissors, or exit')
            continue

        computer_option = random.choice(options)
        print(f"The computer option is: {computer_option}")         

        result = determine_winner(user_option, computer_option)

        if result == "tie":
            print("It's a tie!")
        elif result == "win":
            print("You win!")
        else:
            print("Oh no! You lost!")
        
        print()

if __name__ == "__main__":
    play_game()
