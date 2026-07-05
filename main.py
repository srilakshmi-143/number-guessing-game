import random


def play_game():
    print("\n" + "=" * 40)
    print("      NUMBER GUESSING GAME")
    print("=" * 40)

    print("\nChoose Difficulty")
    print("1. Easy (1-10, 5 attempts)")
    print("2. Medium (1-50, 7 attempts)")
    print("3. Hard (1-100, 10 attempts)")

    choice = input("Enter your choice: ")

    if choice == "1":
        max_num = 10
        attempts = 5
        level = "Easy"

    elif choice == "2":
        max_num = 50
        attempts = 7
        level = "Medium"

    elif choice == "3":
        max_num = 100
        attempts = 10
        level = "Hard"

    else:
        print("Invalid Choice!")
        return

    secret = random.randint(1, max_num)

    total_attempts = attempts
    score = 100

    print(f"\nGuess a number between 1 and {max_num}")

    while attempts > 0:

        print(f"\nAttempt {total_attempts - attempts + 1} of {total_attempts}")

        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > max_num:
                print(f"Please enter a number between 1 and {max_num}.")
                continue

        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess == secret:

            used = total_attempts - attempts + 1

            print("\n🎉 Congratulations!")
            print("You guessed the correct number.")
            print("Your Score:", score)

            print("\n========== GAME SUMMARY ==========")
            print("Difficulty     :", level)
            print("Correct Number :", secret)
            print("Attempts Used  :", used)
            print("Result         : Won")
            print("==================================")

            return

        elif guess < secret:

            if secret - guess <= 5:
                print("Too Low! 🔥 Very Close!")
            else:
                print("Too Low!")

        else:

            if guess - secret <= 5:
                print("Too High! 🔥 Very Close!")
            else:
                print("Too High!")

        attempts -= 1
        score -= 10

        print("Attempts Left:", attempts)

    print("\n😢 Game Over!")
    print("The correct number was:", secret)

    print("\n========== GAME SUMMARY ==========")
    print("Difficulty     :", level)
    print("Correct Number :", secret)
    print("Attempts Used  :", total_attempts)
    print("Result         : Lost")
    print("==================================")


while True:

    play_game()

    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again != "yes":
        print("\nThank you for playing! 😊")
        break