import os


def save_score(score):
    with open("high_score.txt", "w") as file:
        file.write(str(score))


def get_score():
    if not os.path.exists("high_score.txt"):
        save_score(0)
        return 0

    with open("high_score.txt", "r") as file:
        score = file.read().strip()

    if not score.isdigit():
        save_score(0)
        return 0

    return int(score)
