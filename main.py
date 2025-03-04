from stats import get_num_words, sort_dict, get_char_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        num_words = get_num_words(file_contents)
        char_count = get_char_count(file_contents)
        return num_words, char_count

def main():
    num_words, char_count = get_book_text('./books/frankenstein.txt')
    char_count = sort_dict(char_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f'Found {num_words} total words')
    print("--------- Character Count -------")
    for item in char_count:
        if item["char"].isalpha() == True:
            print(f"{item['char']}: {item['count']}")
    print("============= END ===============")

main()