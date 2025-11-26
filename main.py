path_book = "./books/frankenstein.txt"


def get_book_text(book_path):
    book_content = ""
    with open(book_path) as f:
        book_content = f.read()
    return book_content


def get_words_count(content: str):
    splitted = content.split()
    return f"Found {len(splitted)} total words."


def main():
    content = get_book_text(path_book)
    print(get_words_count(content))


main()
