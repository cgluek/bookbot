from stats import get_num_words, sort_dict, get_char_count
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        num_words = get_num_words(file_contents)
        char_count = get_char_count(file_contents)
        return num_words, char_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
    else:
        num_words, char_count = get_book_text(str(sys.argv[1]))
        char_count = sort_dict(char_count)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        print(f'Found {num_words} total words')
        print("--------- Character Count -------")
        for item in char_count:
            if item["char"].isalpha() == True:
                print(f"{item['char']}: {item['count']}")
        print("============= END ===============")

main()