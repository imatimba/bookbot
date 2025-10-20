from stats import get_book_word_count
from stats import get_book_char_count
from stats import sorted_char_count
import sys


def get_book_text(filepath):
    book_text = ""
    with open(filepath) as file:
        book_text = file.read()

    return book_text


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)
    word_count = get_book_word_count(text)
    char_count = get_book_char_count(text)
    sorted_char_list = sorted_char_count(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for c in sorted_char_list:
        print(f"{c['char']}: {c['num']}")

    print("============= END ===============")


main()
