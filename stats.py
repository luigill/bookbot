def get_num_words(content: str):
    splitted = content.split()
    return f"Found {len(splitted)} total words."


def get_num_chars(content: str):
    char_cout = {}

    for i in content:
        processing_char = i.lower()
        # verify if the key that is being processed already exists
        if processing_char not in char_cout.keys():
            char_cout[processing_char] = 1
        else:
            char_cout[processing_char] += 1

    return char_cout


# Auxiliar function of sorting
def sort_on(dictionary: dict):
    return dictionary["num"]


def sort_chars(dictionary: dict):
    list_dicts = []
    for key, value in dictionary.items():
        list_dicts.append(dict(char=key, num=value))
    list_dicts.sort(key=sort_on, reverse=True)
    return list_dicts


def print_chars_count(list_of_dict: list):
    for i in list_of_dict:
        if not i["char"].isalpha():
            continue
        else:
            print(f"{i['char']}: {i['num']} ")
