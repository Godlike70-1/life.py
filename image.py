import random

def get_user_choice():
    user_choice = input("Enter your choice (Snake/Water/Gun): ").strip().lower()
    while user_choice not in ["snake", "water", "gun"]:
        print("Invalid choice. Please enter Snake, Water, or Gun.")
        user_choice = input("Enter your choice (Snake/Water/Gun): ").strip().lower()
    return user_choice

def get_computer_choice():
    choices = ["snake", "water", "gun"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "snake":
        return "You win!" if computer_choice == "water" else "Computer wins!"
    elif user_choice == "water":
        return "You win!" if computer_choice == "gun" else "Computer wins!"
    elif user_choice == "gun":
        return "You win!" if computer_choice == "snake" else "Computer wins!"

def play_game():
    print("Welcome to Snake Water Gun Game!")
    print("You are playing against the computer.")
    print("Choices: Snake, Water, Gun")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {user_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    play_game()
