def count_words(string):
    word_list = string.split()

    return len(word_list)


def count_chars(string):

    result_count = {}

    lower_string = string.lower()

    for letter in lower_string:
        if letter not in result_count:
            result_count[letter] = 0
            result_count[letter] += 1
        else:
            result_count[letter] += 1

    return result_count

def sort_on(dict):
    return dict["count"]

def dict_to_sorted_list(dict):

    char_list = []

    for char, count in dict.items():
        char_list.append({"char": char, "count":count})

    char_list.sort(reverse=True, key=sort_on)

    return char_list







