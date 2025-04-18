from stats import get_num_words

def get_book_text(filepath):
    with open(filepath) as f:
        book = f.read()
    return book

def main():
    book = get_book_text("books/frankenstein.txt")
    word_count = get_num_words(book)
    print(f"{word_count} words found in the document")

main()
