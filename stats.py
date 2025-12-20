def count_words(book):
    word_count = book.split()
    return len(word_count)

def unique_char_count(book):
    unique_char_dict = {}
    book = book.lower()
    for i in book:
        if i in unique_char_dict:
            unique_char_dict[i] += 1
        else:
            unique_char_dict[i] = 1
    return unique_char_dict

def sort_on(items):
    return items["num"]

def list_dict(book_dict):
    dict_list = []
    for i in book_dict:
        dict_list.append({"char":i,"num":book_dict[i]})
    return dict_list

def sort_dict(list):
    list.sort(reverse=True, key=sort_on)
    return list