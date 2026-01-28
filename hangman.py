import random

# get player name
name = input("What is your name? ")
print("Good luck,", name)

# list of possible words
words = [
    'rainbow', 'computer', 'science', 'programming',
    'python', 'mathematics', 'player', 'condition',
    'reverse', 'water', 'board', 'geeks'
]

# pick a random word for the game
word = random.choice(words)

print("Guess the characters")

guesses = ''   # store all guessed characters
turns = 12    # number of allowed wrong guesses

while turns > 0:
    failed = 0

    # show the current state of the word
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    print()

    # if no characters are missing, player wins
    if failed == 0:
        print("You win!")
        print("The word is:", word)
        break

    # get user input
    guess = input("Guess a character: ").lower()

    # basic input check
    if len(guess) != 1:
        print("Please enter a single character.")
        continue

    # avoid counting the same guess twice
    if guess in guesses:
        print("You already guessed that character.")
        continue

    guesses += guess

    # wrong guess reduces remaining turns
    if guess not in word:
        turns -= 1
        print("Wrong!")
        print("You have", turns, "guesses left")

        if turns == 0:
            print("You lose!")
            print("The word was:", word)
