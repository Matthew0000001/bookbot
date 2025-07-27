
# return word count of string
def get_num_words(text):
    return len(text.split())

# compiles dictionary of characters and their number of appearances in text
def get_char_dict(text):
    text = text.lower()
    unique = list(text)
    dictionary = {}
    for char in unique:
        dictionary[char] = text.count(char)
    return dictionary

# key function for sorting below
def sort_on(items):
    return items["num"]

# turns character dictionary into list of character-frequency dictionaries
def get_sorted_dicts(dictionary):
    sorted = []
    for k in dictionary.keys():
        d = {}
        d["char"] = k
        d["num"] = dictionary[k]
        sorted.append(d)
    sorted.sort(reverse=True, key=sort_on)
    return sorted