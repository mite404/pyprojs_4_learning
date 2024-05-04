import random


def play():
    user = input("plz input\n"
                 "'r' for rock\n"
                 "'p' for paper\n"
                 "'s' for scissors\n"
                 "")

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print("it's a tie!")

    # r > s, s > p, p > r
    if is_win(user, computer):
        return "You won!"
    return "You lost!"


def is_win(player, opponent):

    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True


print(play())
