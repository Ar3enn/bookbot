def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        print(f"Analyzing book found at {filepath}")
        return f.read()

def count_words(file_contents: str) -> int:
    return len(file_contents.split()) 

def count_chars(file_contents: str) -> list:
    chars = file_contents.lower()
    chars_dict = {}
    
    for char in chars:
        if not char.isalpha():
            continue
        if char not in chars_dict:
            chars_dict[char] = 1
        else:
            chars_dict[char] += 1   
    
    chars_list = [{"char": char, "num": count} for char, count in chars_dict.items()]
    return chars_list

def get_count(item):
    return item["num"]

def display_sorted(file_contents: str):
    chars_list = count_chars(file_contents)
    chars_list.sort(key=get_count, reverse=True)
    for item in chars_list:
        print(f"{item['char']} : {item['num']}")

