from stats import count_words, unique_char_count

def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content

def main():
    book_content = get_book_text("./books/frankenstein.txt")
    word_count = count_words(book_content)
    unique_chars = unique_char_count(book_content)
    print(f"Found {word_count} total words")
    print(unique_chars)
    return 

main()