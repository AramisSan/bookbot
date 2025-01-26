def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = get_num_words(text)
    char_count = get_num_char(text)
    
#converts char_count into a list of dictionaries 
    char_list = []
    for char in char_count:
        char_list.append({"char": char, "num": char_count[char]})
    
#sorts list
    char_list.sort(reverse=True, key=sort_on)

# prints report
    print_report(num_words, char_list, book_path)

#prints a report for all the information
def print_report(num_words, char_list, path):
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document\n")
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")

# defines sort
def sort_on(num_char):
    return num_char["num"]

#counts how often each characther occurs in text
def get_num_char(text):
    lowered_text = text.lower()
    char_count = {}
    for char in lowered_text:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    return char_count

#gets word count
def get_num_words(text):
    words = text.split()
    return len(words)

#gets the text or returns error message
def get_text(path):
        with open(path) as f:
            return f.read()

main()