from stats import *
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    text = str(get_book_text(filepath))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(get_words_number(text))
    print("--------- Character Count -------")
    char_num = get_char_number(text)
    sort_list = sort_dict(char_num)
    for char in sort_list:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['value']}")
    print("============= END ===============")


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


if __name__ == "__main__":
    main()
