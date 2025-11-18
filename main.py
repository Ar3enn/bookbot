from stats import *
    
def main():
    print("============ BOOKBOT ============")
    text = get_book_text("./books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")
    display_sorted(text)
    print("============= END ===============")


main()    