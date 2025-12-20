def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content

def count_words(book):
    word_count = book.split()
    return len(word_count)

def main():
    book_content = get_book_text("./books/frankenstein.txt")
    return print(f"Found {count_words(book_content)} total words")

main()