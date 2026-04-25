import random       #Random module to generate random numbers

def choose_difficulty():        #Function to choose difficulty level
    print("\nChoose Difficulty:")
    print("1. Easy (1–50, 10 attempts)")
    print("2. Medium (1–100, 7 attempts)")
    print("3. Hard (1–200, 5 attempts)")

    while True:         #Loop until a valid choice is made
        choice = input("Enter choice (1/2/3): ")
        if choice == "1":
            return 50, 10
        elif choice == "2":
            return 100, 7
        elif choice == "3":
            return 200, 5
        else:
            print("Invalid choice. Try again.")

def get_hint(secret, guess):        #Function to provide hints based on the guess
    if abs(secret - guess) <= 5:
        return "Very close!"
    elif abs(secret - guess) <= 15:
        return "Getting warmer."
    else:
        return "Far away."

def play_game():            #Main game function
    max_num, attempts = choose_difficulty()
    secret_number = random.randint(1, max_num)
    score = attempts * 10

    print(f"\nI have chosen a number between 1 and {max_num}.")
    print(f"You have {attempts} attempts to guess it.")

    for attempt in range(1, attempts + 1):      #Loop to allow user attempts
        try:
            guess = int(input(f"\nAttempt {attempt}: Enter your guess: "))
        except ValueError:          #Handle non-numeric input
            print("Please enter a valid number.")
            continue

        if guess < 1 or guess > max_num:
            print(f"Guess must be between 1 and {max_num}.")
            continue

        if guess == secret_number:
            print(f"Correct! You guessed it in {attempt} attempts.")
            print(f"Your score: {score}")
            return score
        elif guess < secret_number:
            print("Too low!", get_hint(secret_number, guess))
        else:
            print("Too high!", get_hint(secret_number, guess))

        score -= 10

    print(f"\nYou ran out of attempts. The number was {secret_number}.")
    return 0

def main():         #Runs the main game loop
    total_score = 0

    print("Welcome to the Number Guessing Game!")

    while True:             #Loop to allow multiple games
        total_score += play_game()
        print(f"\nTotal Score: {total_score}")

        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":          #Entry point of the program
    main()                          #Start the game