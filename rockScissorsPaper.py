import random


def play():
    user = input(" whats your choice ? "
                 "'r' for rock , 's' for scissors , 'p' for paper : ").lower()
    computer = random.choice(['r', 's', 'p'])

    if user == computer:
        return "tie"
    if is_win(user, computer):
        return "you Won"

    return "you Lost"


def is_win(player, opponent):
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (
            player == "p" and opponent == "r"):
        return True


print(play())
