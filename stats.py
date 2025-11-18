def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def count_words(file_contents: str):
     return len(file_contents.split()) 
 
def count_chars(file_contents: str):
    chars = file_contents.lower()
    chars_dict = {}
    for char in chars:
        if char not in chars_dict:
            chars_dict[char] = 1
        elif char in chars_dict:
            chars_dict[char] += 1    
        
    print(chars_dict)
        
        
    
