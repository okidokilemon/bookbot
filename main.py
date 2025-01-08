def main():
    filepath = "books/frankenstein.txt"
    text_book = get_book_text(filepath)
    nb_char = get_occu_char(text_book)
    make_report(filepath, get_nb_words(text_book), nb_char)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_nb_words(text):
    return len(text.split())

def get_occu_char(text):
    lowered_text = text.lower()
    char_count = {}
    for char in lowered_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def make_report(filepath, words_len, dic_occur_char):
    dic_occur_char = dict(sorted(dic_occur_char.items(), reverse=True, key=lambda item: item[1]))
    print(f"--- Begin report of {filepath} ---")
    print(f"{words_len} words found in the document\n")
    for k, v in dic_occur_char.items():
        if k.isalpha() == True :
            print(f"The '{k}' character was found {v} times")
    print("--- End report ---")

main()
