import sys

from stats import get_num_chars, get_num_words, print_chars_count, sort_chars

print("Usage: python3 main.py <path_to_book>")

if len(sys.argv) != 2:
    sys.exit(1)
else:
    path_book = sys.argv[1]

# path_book = "./books/frankenstein.txt"


def get_book_text(book_path):
    book_content = ""
    with open(book_path, encoding="utf-8-sig") as f:
        book_content = f.read()
    return book_content


def main():
    content = get_book_text(path_book)
    print(get_num_chars(content))
    # print(sort_chars(get_num_chars(content)))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_book}...")
    print("----------- Word Count ----------")
    print(get_num_words(content))
    print("--------- Character Count -------")
    print_chars_count(sort_chars(get_num_chars(content)))
    print("============= END ===============")


main()
