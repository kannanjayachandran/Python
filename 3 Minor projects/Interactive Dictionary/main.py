import json
from difflib import get_close_matches


def main():
    print("\tSimple Dictionary\n")
    word = input("Enter word: ")

    file_path = "dictionary.json"
    with open(file_path) as file:
        dict_data = json.load(file)

    output = translate(word, dict_data)

    if type(output) == list:
        for i in output:
            print(f"-> {i}\n")
    else:
        print(output)


def translate(word, dict_data):
    """
    This function takes a word as input and returns the meaning of the word.
    """

    word = word.lower()

    if word in dict_data:
        return dict_data[word]

    elif len(get_close_matches(word, dict_data.keys())) > 0:
        ans = input("Did you mean %s instead ? \nEnter Y if Yes, N if No\t: " %
                    get_close_matches(word, dict_data.keys())[0])

        if ans.lower() == 'y':
            return dict_data[get_close_matches(word, dict_data.keys())[0]]

        elif ans.lower() == 'n':
            return f"Sorry, couldn't find the word, '{word}'"

        else:
            return "Oops didn't understand that."

    else:
        return f"Sorry, couldn't find the word, '{word}'"


if __name__ == "__main__":
    main()
