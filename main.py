def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = get_num_words(text)
    num_char = get_num_char(text)
    print(num_char)

def get_num_char(text):
    lowered_text = text.lower()
    char_count = {}
    for char in lowered_text:
        if char.isalnum() or char.isspace():
            char_count[char] = char_count.get(char, 0) + 1
    return char_count

def get_num_words(text):
    words = text.split()
    return len(words)


def get_text(path):
    with open(path) as f:
        return f.read()


main()