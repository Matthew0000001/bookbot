import sys
from stats import get_num_words, get_char_dict, get_sorted_dicts

# return file contents as string
def get_book_text(path):
    with open(path) as file:
        return file.read()

# formatting
def print_sorted_dicts(sorted):
    for d in sorted:
        if d["char"].isalpha():
            print(d["char"] + ": " + str(d["num"]))

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book = get_book_text(path)

    # print char dictionary report
    print("============ BOOKBOT ============\nAnalyzing book found at " + path + "...\n----------- Word Count ----------")
    print("Found " + str(get_num_words(book)) + " total words")
    print("--------- Character Count -------")
    print_sorted_dicts(get_sorted_dicts(get_char_dict(book)))
    print("============= END ===============")

main()