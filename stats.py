def analyze_book(filepath):
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


def get_words_number(text):
    split_text = text.split()
    count = 0
    for _ in split_text:
        count += 1
    return f"Found {count} total words"


def get_char_number(text):
    chars = {}
    for char in text.lower():
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars


def sort_on(dict):
    return dict["value"]


def sort_dict(dict):
    char_list = []
    for key, value in dict.items():
        char_list.append({"char": key, "value": value})
    char_list.sort(reverse=True, key=sort_on)
    return char_list


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
