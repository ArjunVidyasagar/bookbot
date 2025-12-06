import sys
def word_count(file):
    text = open(file).read()
    words = text.split() 
    count = len(words)
    return f"Found {count} total words"

def character_count(file):
    text = open(file).read()
    text_lower = text.lower()
    characters = list(text_lower)
    count_dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, "r": 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0, ' ': 0, '?': 0, '.': 0, '!': 0, ',': 0, '-': 0, ':': 0, ";": 0, "&": 0, "(": 0, ")": 0, "$": 0, "%": 0}
    for char in characters:
        if char in count_dict:
            count_dict[char] += 1
    return count_dict

def sort_on(items):
    return items["num"]

def sort_dict_list(dictionary):
    unsort_list = []
    for key, value in dictionary.items():
        print_dict = {
            "char" : key,
            "num" : value
        }
        unsort_list.append(print_dict)
    unsort_list.sort(reverse=True, key=sort_on)
    for item in unsort_list:
        if item["char"].isalpha() == True:
            print(f"{item["char"]}: {item["num"]}")