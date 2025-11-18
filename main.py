from stats import *
import sys
    
def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    print("============ BOOKBOT ============")
    text = get_book_text(sys.argv[1])
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")
    display_sorted(text)
    print("============= END ===============")
   
    

main()    