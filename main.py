from stats import *
    
def main():
    text = get_book_text("./books/frankenstein.txt")
    print(f"Found {count_words(text)} total words")
    count_chars(text)


main()    