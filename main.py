from stats import count_words, unique_char_count, sort_dict, list_dict, chars_dict_to_sorted_list
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content

def main():
    book_content = get_book_text("./books/frankenstein.txt")
    word_count = count_words(book_content)
    unique_chars = unique_char_count(book_content)
    list_d = list_dict(unique_chars)
    sorted_list = sort_dict(list_d)
    new_dict = chars_dict_to_sorted_list(unique_chars)
    print(f"Found {word_count} total words")
    for i in sorted_list:
            if i["char"].isalpha():
                 print(f"{i["char"]}: {i["num"]}")
    print(new_dict)
    
    return 

#if len(sys.argv) < 2:
#    print("Usage: python3 main.py <path_to_book>")
#    sys.exit(1)
#else:
main()

