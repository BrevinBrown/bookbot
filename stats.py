def get_num_words(book):
    tmp = book.split()
    return len(tmp)

def get_character_count(text):
    character_count = {}
    text = text.lower()
    for character in text:
        if character in character_count:
            character_count[character] +=1
        else:
            character_count[character] = 1
    return character_count

def sort_on(dict):
    return dict["count"]

def sort_characters(dict):
    tmp = []
    for key in dict:
        tmp.append({"character": key, "count": dict[key]})
    tmp.sort(reverse=True, key=sort_on)
    return tmp