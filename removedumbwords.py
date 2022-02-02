def has_repeat(words):
    new_words = []
    for word in words:
        valid_word = True
        for ch in word:
            if word.count(ch) > 1:
                valid_word = False
        if valid_word:
            new_words.append(word)
    return new_words

if __name__ == "__main__":
    with open("fiveletterwords.txt") as file:
        valid_words = [line.rstrip().upper() for line in file]
    better_words = has_repeat(valid_words)
    wordlist = open("betterwords.txt", "w")
    for elem in better_words:
        wordlist.write(elem + "\n")
    wordlist.close()
    