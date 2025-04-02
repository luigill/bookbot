from stats import count_words 
from stats import count_chars 
from stats import dict_to_sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def main():
    file_path = "./books/frankenstein.txt"
    book = get_book_text(file_path)
    result_dict = count_chars(book)
    sorted_chars = dict_to_sorted_list(result_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book)} total words")
    print("--------- Character Count -------")
    for char_entry in sorted_chars:
        print(f"{char_entry["char"]}: {char_entry["count"]}")
    print("============= END ===============")

main()
