import logging
from sys import exit


logging.basicConfig(level=logging.DEBUG)


WORD = ["", "", "", "", "", ]  # orange letters here
NO_LETTERS_AT = ["", "", "", "", "", ]  # blue letters here
HAS_LETTERS = ""  # not tried letters here
HAS_NO_LETTERS = ""  # forbidden letters here


def load_words():
    with open("5-letter-words.txt", "r") as input_file:
        return (line.strip() for line in input_file.readlines())

def with_letters(words, letters):
    return (word for word in words if contains_all(word, letters))

def with_letters_at(words, letters):
    passthrough = False
    if "".join(letters) == "":
        passthrough = True
    for word in words:
        if passthrough:
            yield word
        for i, letter in enumerate(letters):
            if len(letter) > 0:
                if with_letter_at(word, letter, i):
                    yield word


def with_letter_at(word, letter, at):
    return word[at] == letter

def without_letters_at(word, letters, at):
    for letter in letters:
        if word[at] == letter:
            return False
    return True

def without_letters(words, letters):
    return (word for word in words if not contains_any(word, letters))

def without_letter_groups(words, letter_groups):
    for word in words:
        fail = False
        for i, letter_group in enumerate(letter_groups):
            if not without_letters_at(word, letter_group, i):
                fail = True
        if not fail:
            yield word

def contains_any(word, letters):
    for letter in letters:
        if letter in word:
            return True
    return False

def contains_all(word, letters):
    for letter in letters:
        if letter not in word:
            return False
    return True

def main():
    words = list(load_words())
    letters_removed = list(without_letters(words, HAS_NO_LETTERS))
    containing_letters = list(with_letters(letters_removed, HAS_LETTERS))
    containing_letters_at_positions = list(with_letters_at(containing_letters, WORD))
    options = without_letter_groups(containing_letters_at_positions, NO_LETTERS_AT)
    logging.info("options left %s", set(options))
    return 0


if __name__ == "__main__":
    exit(main())