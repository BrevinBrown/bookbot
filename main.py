def get_book_text(filepath):
    with open(filepath) as f:
        book = f.read()
    return book

def main():
    book = get_book_text("books/frankenstein.txt")
    print(book)

main()
