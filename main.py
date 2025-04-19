import sys
from stats import get_num_words, get_character_count, sort_characters

if __name__=="__main__":
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_file_path = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        book = f.read()
    return book

def main():
    book = get_book_text(book_file_path)
    word_count = get_num_words(book)
    
    character_count = get_character_count(book)
    #for character in character_count:
    #    print(f"'{character}': {character_count[character]}")
    sorted_characters = sort_characters(character_count)
    #print(sorted_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for character in sorted_characters:
        if character["character"].isalpha():
            print(f"{character["character"]}: {character["count"]}")
    print("============= END ===============")
    
main()
 