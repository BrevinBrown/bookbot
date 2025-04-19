from stats import get_num_words, get_character_count, sort_characters
book_file_path = "books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath) as f:
        book = f.read()
    return book

def main():
    book = get_book_text(book_file_path)
    word_count = get_num_words(book)
    print(f"{word_count} words found in the document")
    character_count = get_character_count(book)
    #for character in character_count:
    #    print(f"'{character}': {character_count[character]}")
    sorted_characters = sort_characters(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file_path}...")

main()
 