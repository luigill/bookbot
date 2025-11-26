from stats import get_num_words

path_book = "./books/frankenstein.txt"


def get_book_text(book_path):
    book_content = ""
    with open(book_path) as f:
        book_content = f.read()
    return book_content


def main():
    content = get_book_text(path_book)
    print(get_num_words(content))


main()
