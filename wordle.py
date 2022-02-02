import random


def get_wordle(words):
    idx = random.randint(1, len(words) - 1)
    return words[idx]


def update_pointers(guess, correct, pointers):
    for i in range(len(guess)):
        in_word = letter_in_word(guess[i], correct)
        if in_word == 0:
            pointers[i] = "^"
        elif in_word == 1:
            pointers[i] = "|"
    return pointers


def letter_in_word(letter, word):
    for ch in word:
        if ch == letter:
            return 0
    if letter in word:
        return 1
    return 2


def update_letters(guess, correct, letters):
    for ch in guess:
        in_word = letter_in_word(ch, correct)
        if in_word == 1:
            letters[ch] = 1
        elif in_word == 2:
            letters[ch] = 2
    return letters


def run_game(words):
    template, pointers = ["_" for i in range(5)], ["_" for i in range(5)]
    wordle = get_wordle(words)
    correct = False
    guesses = 6
    guessed_words = []
    letters = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0,
               'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0,
               'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0,
               'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

    while guesses > 0 and not correct:
        valid_guess = False
        guess = input("guess a word: ").upper()
        while not valid_guess:
            if len(guess) != 5:
                print("please guess a five-letter word")
                guess = input("guess a word: ").upper()
            elif guess not in words:
                print("word not in word list")
                guess = input("guess a word: ").upper()
            elif guess in guessed_words:
                print("you've already guessed this")
                guess = input("guess a word: ").upper()
            else:
                guessed_words.append(guess)
                valid_guess = True
        pointers = update_pointers(guess, wordle, pointers)
        template = [ch for ch in guess]
        letters = update_letters(guess, wordle, letters)
        print(" ".join(template))
        print(" ".join(pointers))
        print("letters left: ")
        letters_left = []
        for letter in letters:
            if letters[letter] != 2:
                letters_left.append(letter)
        print(" ".join(letters_left))

        if guess == wordle:
            correct = True

        guesses -= 1
    if correct:
        print("nice! you guessed it in " + str(guesses) + "/6 guesses!")
    else:
        print("sorry, word was " + wordle)

    return correct


if __name__ == "__main__":
    with open("fiveletterwords.txt") as file:
        valid_words = [line.rstrip().upper() for line in file]

    wins = 0
    games = 0
    play_game = True
    while play_game:
        win = run_game(valid_words)
        again = input("do you want to play again? y/n: ")
        if again != "y" or again != "Y":
            play_game = False
        if win:
            wins += 1
        games += 1

    print("you played " + str(games) + " games and won " + str(wins) + " times")
