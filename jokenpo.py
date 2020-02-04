import random
import time


# text with time
def print_pause(x):
    print(x)
    time.sleep(0.5)


# intro for the game
def intro():
    print_pause("Hello, let's play Rock, Paper Scissors!!!")


# choosing
def choice(winner, loser, round, moves):

    bot = random.choice(moves)

    print_pause(f"\nROUND {round} ---\n")
    print_pause("Remeber: \n"
                "Rock beats Scissors;\n"
                "Scissors beats Paper;\n"
                "Paper beats Rock.\n")
    player = input("Type Rock\n"
                   "Type Paper\n"
                   "Type Scissors\n"
                   "(E) Exit the game\n"
                   "(A) Reset the Game\n").lower()

    # 1 = Rock; 2 = Paper; 3 = Scissors
    if player in moves:
        results(winner, loser, round, player, moves, bot)
    elif player == 'e':
        print("Thanks for playing... See you soon!!")
    elif player == 'a':
        print_pause("Let's Reset the Game!!\n")
        winner = 0
        loser = 0
        round = 1
        choice(winner, loser, round, moves)
    else:
        error_msg(winner, loser, round, moves)


# results
def results(winner, loser, round, player, moves, bot):
    # show the bot result
    print_pause(f"You play {player} and the PC plays {bot}.\n")

    # 1 = Rock; 2 = Paper; 3 = Scissors
    # tie situation
    if ((player == bot) or
       (player == bot) or
       (player == bot)):
        print_pause("It's a TIE!\n")

    # 1 = Rock; 2 = Paper; 3 = Scissors
    # loose situation
    elif ((player == 'scissors' and bot == 'rock') or
          (player == 'rock' and bot == 'paper') or
          (player == 'paper' and bot == 'scissors')):
        print_pause("You LOOSE!\n")
        loser += 1

    # 1 = Rock; 2 = Paper; 3 = Scissors
    # win situation
    elif ((player == 'paper' and bot == 'rock') or
          (player == 'scissors' and bot == 'paper') or
          (player == 'rock' and bot == 'scissors')):
        print_pause("You WIN!\n")
        winner += 1

    # count round and score
    print_pause(f"Score You:{winner} ; CPU {loser}\n")
    # count for the next round
    round += 1
    choice(winner, loser, round, moves)


# error msg
def error_msg(winner, loser, round, moves):
    print_pause("Sorry, I don't understand.\n")
    choice(winner, loser, round, moves)


# play game
def play_game():
    intro()
    # w = win
    winner = 0
    # l = loose
    loser = 0
    round = 1
    moves = ['rock', 'paper', 'scissors']
    choice(winner, loser, round, moves)


if __name__ == "__main__":
    play_game()
