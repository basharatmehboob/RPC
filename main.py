import random

def play_game():
    choices = ["rock", "paper", "scissors"]

    player_score = 0
    computer_score = 0
    ties = 0

    print("=" * 40)
    print("       ROCK PAPER SCISSORS")
    print("=" * 40)
    print("First to 3 wins takes the match!\n")

    while player_score < 3 and computer_score < 3:

        print(f"\nScore: You {player_score} - {computer_score} Computer")
        print(f"Ties: {ties}")

        print("\nChoose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("Q. Quit")

        choice = input("\nYour choice: ").strip().lower()

        if choice == "q":
            print("\nThanks for playing!")
            return

        if choice not in ["1", "2", "3"]:
            print("Invalid choice! Please try again.")
            continue

        player = choices[int(choice) - 1]
        computer = random.choice(choices)

        print(f"\nYou chose: {player.title()}")
        print(f"Computer chose: {computer.title()}")

        if player == computer:
            print("It's a tie!")
            ties += 1

        elif (
            (player == "rock" and computer == "scissors")
            or (player == "paper" and computer == "rock")
            or (player == "scissors" and computer == "paper")
        ):
            print("You win this round!")
            player_score += 1

        else:
            print("Computer wins this round!")
            computer_score += 1

    print("\n" + "=" * 40)

    if player_score == 3:
        print("CONGRATULATIONS! YOU WON THE MATCH!")
    else:
        print("COMPUTER WON THE MATCH!")

    print(f"\nFinal Score: You {player_score} - {computer_score} Computer")
    print(f"Total Ties: {ties}")
    print("=" * 40)


while True:
    play_game()

    again = input("\nPlay again? (y/n): ").strip().lower()

    if again not in ["y", "yes"]:
        print("\nThanks for playing Rock Paper Scissors!")
        break
