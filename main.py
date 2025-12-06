import sys

def get_book_text(file):
    with open(file) as f:
        contents = f.read()
    return contents

from stats import word_count
from stats import character_count
from stats import sort_on
from stats import sort_dict_list

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)    
    print(f"""============ BOOKBOT ============
    Analyzing book found at {sys.argv[1]}...""")
    print("----------- Word Count ----------")
    print(word_count(sys.argv[1]))

    print("--------- Character Count -------")
    sort_dict_list(character_count(sys.argv[1]))
    print("============= END ===============")

main()