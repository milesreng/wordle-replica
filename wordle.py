import random

def get_wordle(words):
    idx = random.randint(1, len(words) - 1)
    return words[idx]

def update_pointers(guess, correct, pointers):
    for i in range(len(guess)):
        if guess[i] == correct[i]:
            pointers[i] = guess[i]
    return

def letter_in_word(letter, word):
    for ch in word:
        if ch == letter:
            return 0
    if letter in word:
        return 1
    return 2

def run_game(words):
    template, pointers = ["_" for i in range(5)], ["_" for i in range(5)]
    wordle = get_wordle(words)
    correct = False
    guesses = 6
    guessed_words = []

    while guesses > 0 and not correct:
        valid_guess = False
        guess = input("guess a word: ")
        while not valid_guess:
            if len(guess) != 5:
                print("please guess a five-letter word")
                guess = input("guess a word: ")
            elif guess not in words:
                print("word not in word list")
                guess = input("guess a word: ")
            elif guess in guessed_words:
                print("you've already guessed this")
                guess = input("guess a word: ")
            else:
                guessed_words.append(guess)
                valid_guess = True
        
        guess -= 1

if __name__ == "__main__":
    with open("fiveletterwords.txt") as file:
        valid_words = [line.rstrip().upper() for line in file]
    run_game(valid_words)