import random
from config import CHOICES, WINNER, score_board


def get_user_choice():
    user_choice = input('Enter your choice (r, s, p):')
    if user_choice not in CHOICES:
        print("wrong input, select from (r, s, p).")
        return get_user_choice()
    return user_choice


def get_system_choice():
    system_choice = random.choice(CHOICES)
    return system_choice


def find_the_winner(user_choice, system_choice):
    both_choices = (user_choice, system_choice)
    if len(set(both_choices)) == 1:
        return None
    return WINNER[tuple(sorted(both_choices))]


def show_results(result):
    print("#" * 30)
    print("##", f"user: {result['user']} system: {result['system']}",
          "##".rjust(9))
    print("#" * 30)


def update_score_board(result):
    if result['user'] == 3:
        score_board['user'] += 1
    else:
        score_board['system'] += 1


def show_scoreboard():
    print("#" * 30)
    print("##", f"user: {score_board['user']} system: {score_board['system']}",
          "##".rjust(9))
    print("#" * 30)


def play():
    result = {'user': 0, 'system': 0}
    while result['user'] < 3 and result['system'] < 3:
        user_choice = get_user_choice()
        system_choice = get_system_choice()
        winner = find_the_winner(user_choice, system_choice)
        if winner == user_choice:
            result['user'] += 1
        elif winner == system_choice:
            result['system'] += 1
        print("user choice:", user_choice, "system choice:", system_choice,
              "winner: ", winner)
        show_results(result)
    update_score_board(result)
    show_scoreboard()
    play_again = input("Do you want to play again? (y/n):")
    if play_again == "y":
        play()


if __name__ == '__main__':
    play()
