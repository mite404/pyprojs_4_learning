import random
# TODO import random
# TODO define play()
    # TODO ask for user input
    # TODO create random value for computer
    # TODO create tie condition
    # TODO create if statement for win condition
        # TODO print win/loose
# TODO define is_win (here is the logic for the rules of what beats what)
# TODO call play (why is this inside print()? )
#
# r > s / s > p / p > r
#


def play():
    user = input("r / rock\n"
                      "p / paper\n"
                      "s / scissors\n"
                      "throw: \n"
                      "")

    computer = random.choice(['r, p, s'])

    if user == computer:
        print("it's a tie!!")

    # win condition
    # r > s / s > p / p > r
    if is_win(user, computer):
        return "You won!"
    return f"You lost! Computer chose: {computer}"


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True


print(play())
