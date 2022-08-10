import json
from difflib import get_close_matches

dic_data = json.load(
    open("3. PROJECTS\Interactive Dictionary\dictionary.json"))


def translate(word):

    word = word.lower()

    if word in dic_data:
        return dic_data[word]

    elif len(get_close_matches(word, dic_data.keys())) > 0:
        ans = input("Did you mean %s instead ? \nEnter Y if Yes, N if No\t: " %
                    get_close_matches(word, dic_data.keys())[0])

        if ans.lower() == 'y':
            return dic_data[get_close_matches(word, dic_data.keys())[0]]

        elif ans.lower() == 'n':
            return "Sorry, couldn't find the word, '%s'" % word

        else:
            return "Oops didn't understand that."

    else:
        return "Sorry, couldn't find the word, '%s'" % word


print("\n\t\tSimple Dictionary\n")
word = input("Enter word: ")


output = translate(word)

if type(output) == list:
    for i in output:
        print("->", i, "\n")
else:
    print(output)

# End of File
