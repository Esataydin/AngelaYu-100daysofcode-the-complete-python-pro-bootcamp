import random

from art import logo, vs
from game_data import data


def get_random_account() -> list[dict[str, any]]:
    """Gets data from a random Instagram account in game_data file"""
    return random.choice(data)


def format_data(account: dict[str, any]) -> str:
    """Formats account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def check_answer(guess: str, a_followers: int, b_followers: int) -> bool:
    """Checks followers against user's guess
      and returns True if they got it right.
      Or False if they got it wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game() -> None:
    print(logo)
    score: int = 0
    is_winning: bool = True
    account_b = get_random_account()

    while is_winning:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}. Follower Count:{account_a['follower_count']}M")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct: bool = check_answer(guess, a_follower_count, b_follower_count)
        print("\n"*3)

        if is_correct == True:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            is_winning = False
            print(f"A: {format_data(account_a)}. Follower Count:{account_a['follower_count']}M")
            print(f"B: {format_data(account_b)}. Follower Count:{account_b['follower_count']}M")
            print(f"Sorry, that's wrong. Final score: {score}")


def main() -> None:
    while input("\nDo you want to play the game higher or lower? Type 'y' or 'n': ").lower() == 'y':
        game()
    print("\nThanks for playing.")


if __name__ == '__main__':
    main()
