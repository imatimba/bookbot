def get_book_word_count(book_text):
    word_list = book_text.split()
    return len(word_list)


def get_book_char_count(book_text):
    char_dict = {}

    for c in book_text:
        c = c.lower()
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1

    return char_dict


def sorted_char_count(dict):
    char_list = []

    for char in dict:
        if char.isalpha():
            char_list.append({"char": char, "num": dict[char]})

    def sort_on(items):
        return items["num"]

    char_list.sort(reverse=True, key=sort_on)

    return char_list
