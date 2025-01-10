def main():
    bookpath ="books/frankenstein.txt" 
    book = open_book(bookpath)
    num_words = number_of_words(book)
    chars_dict = num_chars(book)
    character_list = char_list(chars_dict)
    character_list.sort(reverse=True, key=sort_on)

    book_report(bookpath, num_words, character_list)


def open_book(path):
    with open(path) as f:
        return f.read()


def number_of_words(text):
    words = text.split()
    return len(words)


def num_chars(text):
    char_dict = {}
    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def char_list(dict):
    chars = []
    for item in dict:
        if item.isalpha():
            chars.append({"character": item, "num": dict[item]})
    return chars


def sort_on(dict):
    return dict["num"]


def char_report(dict):
    return "test"


def book_report(path, wordcount, char_count):
    print(f"--- Begin report of {path} ---")
    print(f"{wordcount} words found in the document\n")
    for char in char_count:
        print(f"The '{char['character']}' character was found {char['num']} times")
    print(f"--- End report ---")
    pass

main()