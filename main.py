"""
Literalnie helper
"""
import logging
import re
import sys
from typing import List


logging.basicConfig(level=logging.DEBUG)


WORD = ["", "", "", "", "", ]  # orange letters here
NO_LETTERS_AT = ["", "", "", "", "", ]  # blue letters here
HAS_NO_LETTERS = ""  # forbidden letters here
NO_DUPLICATES = False
CHECK = ""

ALL_LETTERS = set("qwertyuiopasdfghjklzxcvbnmąćęłńóśźż")


def load_words():
    """Loads words"""
    with open("5-letter-words.txt", "r", encoding="utf8") as input_file:
        return (line.strip() for line in input_file.readlines())


def build_pattern() -> str:
    """Builds regular expression"""
    result = []
    for letter, no_letters in zip(WORD, NO_LETTERS_AT):
        if letter:
            result.append(letter)
        else:
            without_letters = set(no_letters + HAS_NO_LETTERS)
            possibilities = ALL_LETTERS - without_letters
            result.append(f'[{"".join(possibilities)}]')
    return "".join(result)


def match_words(words: List[str], pattern: str):
    """Filter matching words"""
    for word in words:
        if re.match(pattern, word):
            yield word


def print_words(words):
    """Prints words"""
    logging.info("Candidates are %s", list(words))


def remove_duplicates(words):
    """Removes words with letter duplicates"""
    for word in words:
        if len(set(word)) == len(word):
            yield word


def with_check(words):
    """Only words with letters to check"""
    for word in words:
        a_pass = True
        for letter in CHECK:
            if letter not in word:
                a_pass = False
                break
        if a_pass:
            yield word


def with_letters(words):
    """Only words containing confirmed letters"""
    confirmed = "".join(set("".join(NO_LETTERS_AT)))
    for word in words:
        a_pass = True
        for letter in confirmed:
            if letter not in word:
                a_pass = False
                break
        if a_pass:
            yield word


def main():
    """Main function"""
    pattern = build_pattern()
    logging.debug('pattern %s', pattern)
    words = list(load_words())
    candidates = with_letters(match_words(words, pattern))
    if NO_DUPLICATES:
        candidates = remove_duplicates(candidates)
    if CHECK:
        candidates = with_check(candidates)
    print_words(candidates)
    return 0


if __name__ == "__main__":
    sys.exit(main())
