import random
random.seed(1234)

# Constants
ROCK = 1
PAPER = 2
SCISSORS = 3

ASCII_ART = {
    ROCK: """    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)""",
    PAPER: """     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)""",
    SCISSORS: """    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""
}

def greetPlayer() -> str:
    print("Welcome to the rock-paper-scissors game!")
    player_name = input("Insert player name: ")
    print(f"Welcome {player_name}!")
    print("Your opponent is RPS-3PO.")
    print("Game starts...\n")
    return player_name

def showMenu() -> None:
    print("Options:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    print("0 - Quit game")

def getPlayerChoice() -> int:
    choice = input("Your choice: ")
    if choice.isnumeric():
        return int(choice)
    return -1  # invalid choice

def getBotChoice() -> int:
    return random.randint(1, 3)

def choiceName(choice: int) -> str:
    if choice == ROCK:
        return "rock"
    elif choice == PAPER:
        return "paper"
    elif choice == SCISSORS:
        return "scissors"
    return "unknown"

def printChoices(player_name: str, player_choice: int, bot_choice: int) -> None:
    print("\nRock! Paper! Scissors! Shoot!\n")
    print("#" * 25)
    print(f"{player_name} chose {choiceName(player_choice)}.\n")
    print(ASCII_ART[player_choice])
    print("#" * 25)
    print(f"RPS-3PO chose {choiceName(bot_choice)}.\n")
    print(ASCII_ART[bot_choice])
    print("#" * 25)

def determineWinner(player_choice: int, bot_choice: int) -> str:
    if player_choice == bot_choice:
        return "draw"
    if (player_choice == ROCK and bot_choice == SCISSORS) or \
       (player_choice == PAPER and bot_choice == ROCK) or \
       (player_choice == SCISSORS and bot_choice == PAPER):
        return "player"
    return "bot"

def main() -> None:
    print("Program starting.")
    player_name = greetPlayer()

    stats = {"player_wins": 0, "player_losses": 0, "player_draws": 0,
             "bot_wins": 0, "bot_losses": 0, "bot_draws": 0}

    while True:
        showMenu()
        choice = getPlayerChoice()

        if choice == 0:
            break
        if choice not in (ROCK, PAPER, SCISSORS):
            print("Unknown option! Try again.\n")
            continue

        bot_choice = getBotChoice()
        printChoices(player_name, choice, bot_choice)
        winner = determineWinner(choice, bot_choice)

        if winner == "draw":
            print(f"Draw! Both players chose {choiceName(choice)}.\n")
            stats["player_draws"] += 1
            stats["bot_draws"] += 1
        elif winner == "player":
            print(f"{player_name} {choiceName(choice)} beats RPS-3PO {choiceName(bot_choice)}.\n")
            stats["player_wins"] += 1
            stats["bot_losses"] += 1
        else:
            print(f"RPS-3PO {choiceName(bot_choice)} beats {player_name} {choiceName(choice)}.\n")
            stats["player_losses"] += 1
            stats["bot_wins"] += 1

    # Show final results
    print("\nResults:")
    print(f"{player_name} - wins ({stats['player_wins']}), losses ({stats['player_losses']}), draws ({stats['player_draws']})")
    print(f"RPS-3PO - wins ({stats['bot_wins']}), losses ({stats['bot_losses']}), draws ({stats['bot_draws']})\n")

    print("Program ending.")

if __name__ == "__main__":
    main()
