import random
import time
import sys

# ASCII art representations for dice 1-6
DICE_ART = {
    1: (
        "+-------+",
        "|       |",
        "|   o   |",
        "|       |",
        "+-------+"
    ),
    2: (
        "+-------+",
        "| o     |",
        "|       |",
        "|     o |",
        "+-------+"
    ),
    3: (
        "+-------+",
        "| o     |",
        "|   o   |",
        "|     o |",
        "+-------+"
    ),
    4: (
        "+-------+",
        "| o   o |",
        "|       |",
        "| o   o |",
        "+-------+"
    ),
    5: (
        "+-------+",
        "| o   o |",
        "|   o   |",
        "| o   o |",
        "+-------+"
    ),
    6: (
        "+-------+",
        "| o   o |",
        "| o   o |",
        "| o   o |",
        "+-------+"
    )
}


def print_dice(dice_values):
    """Print ASCII art of dice side-by-side."""
    for i in range(5):  # each die has 5 lines
        line = '   '.join(DICE_ART[val][i] for val in dice_values)
        print(line)


def get_valid_input(prompt, valid_options):
    """Ensure input is one of the allowed options."""
    while True:
        user_input = input(prompt).strip()
        if user_input in valid_options:
            return user_input
        print("Invalid input. Try again.")


def roll_dice(num_dice=2):
    """Roll dice and return list of results."""
    return [random.randint(1, 6) for _ in range(num_dice)]


def play_round(player_name):
    """Let a player roll and return the total score."""
    input(f"{player_name}, press Enter to roll the dice...")
    dice = roll_dice()
    print_dice(dice)
    total = sum(dice)
    print(f"{player_name} rolled: {dice} → Total: {total}\n")
    time.sleep(1)
    return total


def play_game(mode, rounds=3):
    """Main game logic."""
    if mode == "1":
        player1 = "You"
        player2 = "Computer"
    else:
        player1 = input("Enter name for Player 1: ")
        player2 = input("Enter name for Player 2: ")

    scores = {player1: 0, player2: 0}

    print(f"\nGame Start! First to {rounds} rounds.\n")
    for round_num in range(1, rounds + 1):
        print(f"--- Round {round_num} ---")
        score1 = play_round(player1)
        if mode == "1":
            time.sleep(1)
        score2 = play_round(player2)

        if score1 > score2:
            print(f"{player1} wins the round!\n")
            scores[player1] += 1
        elif score2 > score1:
            print(f"{player2} wins the round!\n")
            scores[player2] += 1
        else:
            print("It's a tie!\n")

        print(f"Score: {player1} {scores[player1]} - {player2} {scores[player2]}\n")
        time.sleep(1)

    print("=== Game Over ===")
    if scores[player1] > scores[player2]:
        print(f"{player1} wins the game!")
    elif scores[player2] > scores[player1]:
        print(f"{player2} wins the game!")
    else:
        print("The game is a tie!")

    print("\nThanks for playing!\n")


def show_menu():
    """Display main menu and get game mode."""
    print("🎲 Welcome to Dice Game!")
    print("1. Player vs Computer")
    print("2. Player vs Player")
    print("3. Exit")

    choice = get_valid_input("Choose game mode (1/2/3): ", {"1", "2", "3"})
    return choice


def main():
    while True:
        choice = show_menu()
        if choice == "3":
            print("Goodbye!")
            sys.exit()
        play_game(choice)
        again = get_valid_input("Play again? (y/n): ", {"y", "n"})
        if again == "n":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()