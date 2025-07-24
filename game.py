import random

def play_game():
    while True:
        print("Hello and Welcome to Rock, Paper, Scissors!")
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

        if user_option == computer_option:
            print("It's a tie!")
        
        elif (user_option == 'rock' and computer_option == 'scissors') or (user_option == 'paper' and computer_option == 'rock') or (user_option == 'scissors' and computer_option == 'paper'):
            print("You win!")
        
        else:
            print("You lost! Try again!")
        
        print()

play_game()
