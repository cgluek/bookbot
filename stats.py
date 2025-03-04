def get_num_words(book_as_string):
    return len(book_as_string.split())

def get_char_count(book_as_string):
    book_as_string = book_as_string.lower()
    char_dict = {}
    for i in book_as_string:
        if i in char_dict.keys():
            char_dict[i] += 1
        else:
            char_dict[i] = 1
    return char_dict

def sort_on(dict):
    return dict["count"]

def sort_dict(input_dict):
    list_of_dicts = []
    for char, count in input_dict.items():
        list_of_dicts.append({"char":char, "count":count})
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

