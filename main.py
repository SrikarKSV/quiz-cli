from pprint import pprint

import requests


def fetch_quiz(category, num_of_que, difficulty):
    r = requests.get(
        f"https://opentdb.com/api.php?amount={num_of_que}&category={category}&difficulty={difficulty}"
    )

    return r.json().get("results", "There was an error while fetching questions")


if __name__ == "__main__":
    pprint(fetch_quiz(9, 100, "easy"))  # Category for General knowledge
