def has_repeat(words):
    for word in words:
        for ch in word:
            if word.count(ch) > 1:
                words.remove(word)
                break
    return words

if __name__ == "__main__":
    with open("fiveletterwords.txt") as file:
        valid_words = [line.rstrip().upper() for line in file]
    has_repeat(valid_words)
    