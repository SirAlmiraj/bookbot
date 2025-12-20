from stats import count_words, unique_char_count, sort_dict, list_dict, sort_on

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
    print(f"Found {word_count} total words")
    for i in sorted_list:
            if i["char"].isalpha():
                 print(f"{i["char"]}: {i["num"]}")
    return 

main()