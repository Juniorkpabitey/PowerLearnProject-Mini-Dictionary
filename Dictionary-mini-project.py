import json
from difflib import get_close_matches

def load_dictionary():
    with open('data.json') as file:
        data = json.load(file)
    return data

def get_definition(word, dictionary):
    word = word.lower()  # Convert the word to lowercase for case-insensitivity
    if word in dictionary:
        return dictionary[word]
    elif word.title() in dictionary:  # Check for proper nouns
        return dictionary[word.title()]
    elif word.upper() in dictionary:  # Check for acronyms
        return dictionary[word.upper()]
    else:
        # Find close matches using difflib
        close_matches = get_close_matches(word, dictionary.keys(), n=1, cutoff=0.8)
        if close_matches:
            suggestion = close_matches[0]
            response = input(f"Did you mean '{suggestion}' instead of '{word}'? Enter Y for yes, or N for no: ")
            if response.lower() == 'y':
                return dictionary[suggestion]
        return "Word not found. Please double-check your spelling."

def main():
    dictionary = load_dictionary()
    while True:
        word = input("Enter a word to get its definition (Q to quit): ").strip()
        if word.lower() == 'q':
            break
        definition = get_definition(word, dictionary)
        print(definition)

if __name__ == "__main__":
    main()
