import sys
import random

welcome_message = """Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have a few chances to guess the correct number.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

"""

possible_difficulties = {
    "easy": 10,
    "medium": 5,
    "hard": 3,
    "3": 3,
    "5": 5,
    "10": 10,
    "1.": 10,
    "2.": 5,
    "3.": 3
}

replay = False

def main():
    number = random.randint(0, 100)
    print(welcome_message)
    difficulty = ""
    while not difficulty in possible_difficulties:
        difficulty = input("Enter your choice: ").lower()
    difficulty = possible_difficulties[difficulty]
    diff_string = list(possible_difficulties.keys())[list(possible_difficulties.values()).index(difficulty)]

    print(f"Great! You have selected the {diff_string} difficulty level.")
    print("Let's start the game!")
    
    num_tries = 0
    while num_tries <= difficulty:
        try:
            if num_tries == difficulty:
                user_number = int(input("[LAST TRY] Enter your guess: "))
            else:
                user_number = int(input("Enter your guess: "))
        except ValueError:
            pass
        if not number == user_number:
            print("Incorrect! ", f"The number is {"greater" if user_number < number else "less"} than {user_number}")
        else:
            print(f"Congratulations! You guessed the correct number in {num_tries + 1} attempts.")
            sys.exit(0)
        num_tries += 1
        print("\n")

    print(f"It's just bad luck... The correct number would've been: {number}\n")
    
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nAw why u quitting?")
        sys.exit(1)
